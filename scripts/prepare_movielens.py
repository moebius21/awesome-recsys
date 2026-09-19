#!/usr/bin/env python3
"""Convert MovieLens ratings into a stable time-ordered train/valid/test split."""
import argparse
from pathlib import Path
import pandas as pd

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    ratings = pd.read_csv(args.input / "u.data", sep="\\t", names=["user_id", "item_id", "rating", "timestamp"])
    ratings = ratings.sort_values(["user_id", "timestamp"])
    groups = ratings.groupby("user_id", group_keys=False)
    test = groups.tail(1)
    remaining = ratings.drop(test.index)
    valid = remaining.groupby("user_id", group_keys=False).tail(1)
    train = remaining.drop(valid.index)
    args.output.mkdir(parents=True, exist_ok=True)
    train.to_csv(args.output / "train.csv", index=False)
    valid.to_csv(args.output / "valid.csv", index=False)
    test.to_csv(args.output / "test.csv", index=False)
    print(f"train={len(train):,}, valid={len(valid):,}, test={len(test):,}")

if __name__ == "__main__":
    main()
