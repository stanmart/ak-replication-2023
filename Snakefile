import platform


rule prepare_data:
    input:
        data = "data/raw/QOB.txt"
    output:
        data = "data/clean/census_data.csv"
    shell:
        "python src/data/prepare_data.py"


rule extract_data:
    input:
        rar = "data/raw/QOB.rar"
    output:
        data = "data/raw/QOB.txt"
    params:
        mv = "move" if platform.system() == "Windows" else "mv"
    shell:
        "unrar x {input.rar} && {params.mv} QOB {output.data}"


rule download_data:
    output:
        data = "data/raw/QOB.rar"
    shell:
        "http https://economics.mit.edu/sites/default/files/inline-files/QOB.rar --output {output.data}"
