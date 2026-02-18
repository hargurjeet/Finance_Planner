import os
import ssl
from crewai import LLM
from dotenv import load_dotenv
from retirement_planner.config.setting import settings

# Load .env file
load_dotenv(r"C:\Users\614654958\OneDrive - BT Plc\download_one_drive\extra\Git\Finance_Planner\.env")

# Skip SSL certificate validation
os.environ["AWS_CA_BUNDLE"] = r"C:\Users\614654958\OneDrive - BT Plc\download_one_drive\ICM\dcpcli_2.0.4_windows_amd64.pem"
os.environ["REQUESTS_CA_BUNDLE"] = ""
os.environ["CURL_CA_BUNDLE"] = ""
os.environ["SSL_CERT_FILE"] = ""
os.environ["LITELLM_SSL_VERIFY"] = "False"
os.environ["OTEL_SDK_DISABLED"] = "true"
ssl._create_default_https_context = ssl._create_unverified_context

import botocore.httpsession
orig_send = botocore.httpsession.URLLib3Session.send
def patched_send(self, request):
    self._verify = False
    return orig_send(self, request)
botocore.httpsession.URLLib3Session.send = patched_send

import httpx
orig_init = httpx.Client.__init__
def patched_init(self, *args, **kwargs):
    kwargs["verify"] = False
    orig_init(self, *args, **kwargs)
httpx.Client.__init__ = patched_init

os.environ["REGION"] = settings.region

def make_bedrock_llm(
    model_env_var: str = "ANTHROPIC_CLAUDE_3_7_SONNET_20250219_V1_0",
    temperature: float = 0.3,
    top_p: float = 0.1,
    max_tokens: int = 2048,
    region: str = "eu-west-2"
) -> LLM:
    arn = os.environ.get(model_env_var)
    if not arn:
        raise ValueError(f"Environment variable '{model_env_var}' not set.")
    return LLM(
        model=f"bedrock/converse/{arn}",
        region_name=region,
        temperature=temperature,
        top_p=top_p,
        max_tokens=max_tokens
    )

llm = make_bedrock_llm()

def get_llm() -> LLM:
    return llm
