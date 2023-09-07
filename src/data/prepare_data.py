import pandas as pd

def prepare_data(input_path, output_path):
    """Give proper names to the variables and export
    
    Args:
        input_path (str): Path to the raw data
        output_path (str): Path to the processed data
    """
    df = pd.read_csv(input_path, sep= " ", header=None)

    rename_dict = {
        1: "age",
        2: "ageq",
        4: "education",
        5: "enocent",
        6: "esocent",
        9: "log_weekly_wage",
        10: "married",
        11: "midatl",
        12: "mt",
        13: "neweng",
        16: "census",
        18: "quarter_of_birth",
        19: "race",
        20: "smsa",
        21: "soatl",
        24: "wnocent",
        25: "wsocent",
        27: "year_of_birth"
    }

    df = df.rename(columns=rename_dict)
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    prepare_data(
        snakemake.input["data"],
        snakemake.output["data"]
    )
