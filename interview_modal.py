from modal import Stub, Image, method, gpu, Secret, create_package_mounts
from huggingface_hub import snapshot_download
import time
import json
from jinja2 import Template
from interview_cuda import *

def download_model(name, info = {}, **kwargs):
    with open("./_info.json",'w') as f:
        json.dump({"model_name": name, **info}, f)
    snapshot_download(name, **kwargs)

def download_codegen_2p5_7b_mono_model():
    download_model("Salesforce/codegen25-7b-mono")

def download_codegen_2p5_7b_multi_model():
    download_model("Salesforce/codegen25-7b-multi")

def download_codegen_2_1b_multi_model():
    download_model("Salesforce/codegen2-1B")

def download_codegen_2_3p7b_multi_model():
    download_model("Salesforce/codegen2-3_7B")

def download_codegen_2_7b_multi_model():
    download_model("Salesforce/codegen2-7B")

def download_falcon_instruct_7b_model():
    download_model("tiiuae/falcon-7b-instruct", allow_patterns=["*.json","*.model","pytorch*.bin"])

def download_replit_code_instruct_3b_model():
    download_model("sahil2801/replit-code-instruct-glaive", info={"eos_token_id": 1 })

def download_replit_code_v1_3b_model():
    download_model("replit/replit-code-v1-3b", info={"generate_args": { "stop_seq": ["###"]}})

def download_replit_codeinstruct_v2_3b_model():
    download_model("teknium/Replit-v2-CodeInstruct-3B", info={"eos_token_id": 1 })

#https://huggingface.co/matorus/replit-openorca

def download_vicuna_1p1_7b_model():
    download_model("lmsys/vicuna-7b-v1.1")

def download_vicuna_1p1_13b_model():
    download_model("lmsys/vicuna-13b-v1.1")

def download_vicuna_1p3_7b_model():
    download_model("lmsys/vicuna-7b-v1.3")

def download_vicuna_1p3_13b_model():
    download_model("lmsys/vicuna-13b-v1.3")

def download_llama2_7b_model():
    download_model("meta-llama/Llama-2-7b-hf", ignore_patterns=["*.bin"])

def download_llama2_chat_7b_model():
    download_model("meta-llama/Llama-2-7b-chat-hf", ignore_patterns=["*.bin"])

def download_llama2_chat_13b_model():
    download_model("meta-llama/Llama-2-13b-chat-hf", ignore_patterns=["*.bin"])

def download_llama2_chat_7b_awq_model():
    download_model("abhinavkulkarni/meta-llama-Llama-2-7b-chat-hf-w4-g128-awq")

def download_llama2_gptq_7b_model():
    download_model("TheBloke/Llama-2-7B-GPTQ")

def download_vicuna_1p3_awq_7b_model():
    download_model("mit-han-lab/vicuna-7b-v1.3-4bit-g128-awq")

def download_llama2_13b_model():
    download_model("meta-llama/Llama-2-13b-hf", ignore_patterns=["*.bin"])

def download_redmond_puffin_preview_13b_model():
    download_model("NousResearch/Redmond-Puffin-13B")

def download_codeCherryPop_7b_model():
    download_model("TokenBender/llama2-7b-chat-hf-codeCherryPop-qLoRA-merged")

def download_codeCherryPy_7b_model():
    download_model('TokenBender/codeCherryPy_7B_llama2')

def download_tinycoderpy_model():
    download_model("bigcode/tiny_starcoder_py", ignore_patterns=["*.bin"])

def download_wizardlm_13b_1p1_model():
    download_model("WizardLM/WizardLM-13B-V1.1")

def download_wizardlm_13b_1p2_model():
    download_model("WizardLM/WizardLM-13B-V1.2")

def download_airoboros_7b_1p4p1_model():
    download_model("jondurbin/airoboros-7b-gpt4-1.4.1-qlora")

def download_airoboros_l2_7b_1p4p1_model():
    download_model("jondurbin/airoboros-l2-7b-gpt4-1.4.1")

def download_airoboros_13b_1p4p1_model():
    download_model("jondurbin/airoboros-13b-gpt4-1.4.1-qlora")

def download_airoboros_l2_13b_1p4p1_model():
    download_model("jondurbin/airoboros-l2-13b-gpt4-1.4.1")

def download_NewHope_model():
    download_model("SLAM-group/NewHope")

def download_dolphin_llama2_7b_model():
    download_model('ehartford/dolphin-llama2-7b')

def download_wizardlm_uncencored_llama2_13b_model():
    download_model('ehartford/WizardLM-1.0-Uncensored-Llama2-13b')

def download_nous_hermes_llama2_13b_model():
    download_model('NousResearch/Nous-Hermes-Llama2-13b')

def download_llama2_coder_7b_model():
    download_model('mrm8488/llama-2-coder-7b', info = { 'generate_args': { 'stop_seq': ["###"] } })

def download_wizardcoder_ct2_model():
    download_model('michaelfeil/ct2fast-WizardCoder-15B-V1.0')

def download_mythomix_l2_13b_model():
    download_model('Gryphe/MythoMix-L2-13b')

def download_huginn_1p2_13b_model():
    download_model('The-Face-Of-Goonery/Huginn-13b-v1.2')

def download_orca_mini_1p3_7b_gptq_model():
    download_model('TheBloke/orca_mini_v3_13B-GPTQ', revision='gptq-4bit-32g-actorder_True')

def download_orca_mini_13b_model():
    download_model('psmathur/orca_mini_v3_13b')

def download_octogeex_model():
    download_model('bigcode/octogeex')

def download_octocoder_model():
    download_model('bigcode/octocoder')

image = (
    Image.from_dockerhub(
        "nvidia/cuda:11.8.0-devel-ubuntu22.04",
        setup_dockerfile_commands=["RUN apt-get update", "RUN apt-get install -y python3 python3-pip python-is-python3 git build-essential"]
    )
    .pip_install(
        "transformers==4.31",
        "tiktoken==0.4.0",
        "bitsandbytes==0.40.1.post1",
        "accelerate==0.21.0",
        "einops==0.6.1",
        "sentencepiece==0.1.99",
        "hf-transfer~=0.1",
        index_url="https://download.pytorch.org/whl/cu118",
        extra_index_url="https://pypi.org/simple"
    )  
    .pip_install(
        "vllm @ git+https://github.com/vllm-project/vllm.git@d7a1c6d614756b3072df3e8b52c0998035fb453f",
        index_url="https://download.pytorch.org/whl/cu118",
        extra_index_url="https://pypi.org/simple"
    )
    .env({"HF_HUB_ENABLE_HF_TRANSFER": "1"})
    .pip_install("scipy", "pyarrow")
    .env({"GITHUB_ACTIONS": "true", "TORCH_CUDA_ARCH_LIST": "8.0 8.6 8.9 9.0"})
    .pip_install(
        "auto-gptq @ git+https://github.com/PanQiWei/AutoGPTQ@45576f0933f5e9ef7c1617006d5db359e1669155",
        index_url="https://download.pytorch.org/whl/cu118",
        extra_index_url="https://pypi.org/simple"
    )
    .run_commands(
        "git clone https://github.com/turboderp/exllama /repositories/exllama && cd /repositories/exllama && git checkout cade9bc5576292056728cf55c0c9faf4adae62f8"
    )
    .run_commands("git clone https://github.com/mit-han-lab/llm-awq",
                  "cd llm-awq && git checkout 71d8e68df78de6c0c817b029a568c064bf22132d && pip install -e .",
                  "cd llm-awq/awq/kernels && python setup.py install"
    )
    .pip_install('hf-hub-ctranslate2>=2.0.8','ctranslate2>=3.16.0')
    ##### SELECT MODEL HERE ##############
    .run_function(download_octocoder_model, secret=Secret.from_name("my-huggingface-secret"))
    ######################################
)
stub = Stub(image=image)

##### SELECT RUNTIME HERE #############
#RUNTIME = "transformers"
#QUANT = QUANT_FP16
#RUNTIME = "ctranslate2"
RUNTIME = "vllm"
#RUNTIME = "autogptq"
#RUNTIME = "exllama"
#RUNTIME = "awq"
#######################################

##### SELECT GPU HERE #################
#gpu_request = gpu.T4(count=1)
gpu_request = gpu.A10G(count=2)
#gpu_request = gpu.A100(count=1)
#######################################

@stub.cls(gpu=gpu_request, concurrency_limit=1, container_idle_timeout=300, secret=Secret.from_name("my-huggingface-secret"), mounts=create_package_mounts(["interview_cuda"]))
class ModalWrapper:
    def __enter__(self):
        self.info = json.load(open('./_info.json'))

        if RUNTIME == "transformers":
            self.wrapper = InterviewTransformers(self.info['model_name'], self.info, quant=QUANT)
        elif RUNTIME == "vllm":
            gpu_split = 2 if gpu_request.count == 2 else None
            print(gpu_split)
            self.wrapper = InterviewVLLM(self.info['model_name'], self.info, gpu_split=gpu_split)
        elif RUNTIME == "autogptq":
            self.wrapper = InterviewAutoGPTQ(self.info['model_name'], self.info)
        elif RUNTIME == "exllama":
            gpu_split = '17,24' if gpu_request.count == 2 else None
            self.wrapper = InterviewExllama(self.info['model_name'], self.info, gpu_split=gpu_split)
        elif RUNTIME == "awq":
            if self.info.get('big_model'):
                gpu_split = '0,1' if gpu_request.count == 2 else '0,cpu'
            else:
                gpu_split = None
            self.wrapper = InterviewAWQ(self.info['model_name'], self.info, gpu_split=gpu_split)
        elif RUNTIME == "ctranslate2":
            self.wrapper = InterviewCtranslate2(self.info['model_name'], self.info)
        else:
            raise Exception("Unknown RUNTIME")

        self.wrapper.load()

    @method()
    def generate(self, prompt, params):
        #x
        return self.wrapper.generate(prompt, params)

# For local testing, run `modal run -q interview_modal.py --input results/prepare.ndjson --params params/precise.json`
@stub.local_entrypoint()
def main(input: str, params: str, iterations: int = 1, templateout: str = ""):
    from prepare import save_interview
    from interview_cuda import interview_run

    output_template = Template(open(templateout).read()) if templateout else None

    tasks = []
    for param_file in params.split(','):
        for input_file in input.split(','):
            if param_file != '' and input_file != '':
                tasks.append((param_file, input_file))

    model = ModalWrapper()

    for param_file, input_file in tasks:
      interview = [json.loads(line) for line in open(input_file)]
      params_json = json.load(open(param_file,'r'))

      for iter in range(iterations):
        print(f"Starting iteration {iter} of {param_file} {input_file}")
        results, remote_info = interview_run(RUNTIME, model.generate.call, interview, params_json, output_template, batch=(RUNTIME=="vllm") )
        save_interview(input_file, templateout if templateout else 'none', param_file, remote_info['model_name'], results)
