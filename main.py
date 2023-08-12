import pandas as pd
import itertools

def read_slot_document():
    with open("./Input.xlsx", "rb") as fd:
        return pd.read_excel(fd, sheet_name="slots")

def read_salary_document():
    with open("./Input.xlsx", "rb") as fd:
        df = pd.read_excel(fd, sheet_name="salaries")
    return _create_map_from_columns(df, "Player", "Salary")

def read_settings_document():
    with open("./Input.xlsx", "rb") as fd:
        df = pd.read_excel(fd, sheet_name="settings")
    return _create_map_from_columns(df, "Setting", "Value")
def permute_player_slots(df, salary_df, max_salary):
    column_names = list(df.columns.values)
    transposed_df = df.values.transpose()
    player_list_by_cols = transposed_df.tolist()
    df = pd.DataFrame(list(itertools.product(*player_list_by_cols)), columns=column_names)
    df = df.dropna(axis='index', how='any')
    df["sorted"] = df.apply(lambda row: ",".join(sorted(row)), axis=1, result_type='reduce')
    df = df.drop_duplicates(subset=["sorted"])
    df = df.drop(columns=["sorted"])
    non_unique_mask = df.nunique(axis=1) >= len(df.columns)
    df = df.loc[non_unique_mask, :]

    df = remove_expensive_lineups(df, salary_df, max_salary)

    return df

def remove_expensive_lineups(df, salary_map, max_salary):
    original_cols = df.columns
    salary_cols = []
    for column in original_cols:
        if "Slot" in column:
            new_col_name = column.replace("Slot", "Salary")
            salary_cols.append(new_col_name)
            df[new_col_name] = df[column].map(salary_map)
    df["Total Salary"] = df[salary_cols].sum(axis=1)
    expense_mask = df["Total Salary"] <= max_salary
    df = df.loc[expense_mask, :]
    df = df.drop(columns=salary_cols)
    return df

def generate_output_csv(df):
    df.to_csv("./lineups.csv", index=False)


def _create_map_from_columns(df, col1, col2):
    return dict(zip(df[col1], df[col2]))


def main():
    settings_map = read_settings_document()
    salary_map = read_salary_document()
    slot_df = read_slot_document()
    # print(type(settings_map), type(salary_map), type(slot_df))
    output_df = permute_player_slots(slot_df, salary_map, max_salary=settings_map.get("max_salary"))
    generate_output_csv(output_df)

if __name__ == '__main__':
    main()