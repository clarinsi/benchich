import subprocess

subprocess.run(
    "curl --remote-name-all https://www.clarin.si/repository/xmlui/bitstream/handle/11356/1868{/ParlaSent_BCS.jsonl,/ParlaSent_BCS_test.jsonl}",
    shell=True,
    check=True,
)
