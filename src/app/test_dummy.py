import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Skip SSL verification
os.environ['AWS_CA_BUNDLE'] = r'C:\Users\614654958\OneDrive - BT Plc\download_one_drive\ICM\dcpcli_2.0.4_windows_amd64.pem'
os.environ["REQUESTS_CA_BUNDLE"] = ""
os.environ["CURL_CA_BUNDLE"] = ""
os.environ["SSL_CERT_FILE"] = ""
os.environ["LITELLM_SSL_VERIFY"] = "False"
os.environ["OTEL_SDK_DISABLED"] = "true"

import ssl
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

from crewai import Agent, Task, Crew, LLM

# Setup LLM
os.environ["ANTHROPIC_CLAUDE_3_7_SONNET_20250219_V1_0"] = "arn:aws:bedrock:eu-west-2:767397757887:application-inference-profile/2ldk4c6iwoi7"
arn = os.environ["ANTHROPIC_CLAUDE_3_7_SONNET_20250219_V1_0"]

llm = LLM(
    model=f"bedrock/converse/{arn}",
    region_name="eu-west-2",
    temperature=0.3,
    top_p=0.1,
    max_tokens=2048
)

# Create dummy agent
agent = Agent(
    role="Test Agent",
    goal="Say hello",
    backstory="A simple test agent",
    llm=llm,
    verbose=True
)

# Create task
task = Task(
    description="Say hello in one sentence",
    expected_output="A greeting",
    agent=agent
)

# Run crew
crew = Crew(agents=[agent], tasks=[task], verbose=True)
result = crew.kickoff()

print(f"\n✓ Result: {result}")
