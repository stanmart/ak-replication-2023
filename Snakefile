rule download_data:
    output:
        data = "data/raw/QOB.rar"
    shell:
        "http https://economics.mit.edu/sites/default/files/inline-files/QOB.rar --output {output.data}"
