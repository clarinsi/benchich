import subprocess

subprocess.run(
    "curl --remote-name-all https://www.clarin.si/repository/xmlui/bitstream/handle/11356/1868{/ParlaSent_BCS.jsonl,/ParlaSent_CZ.jsonl,/ParlaSent_EN.jsonl,/ParlaSent_SK.jsonl,/ParlaSent_BCS_test.jsonl,/ParlaSent_EN_test.jsonl,/ParlaSent_SL.jsonl}",
    shell=True,
    check=True,
)
