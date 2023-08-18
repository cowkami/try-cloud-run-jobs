from datetime import date, datetime, timezone, timedelta
import argparse


def create(from_date: str, to_date: str):
    print(f"{from_date} -> {to_date}")
    print("created!")


def delete(from_date: str, to_date: str):
    print(f"{from_date} -> {to_date}")
    print("deleted!")


def date_isoformat(s: str) -> str:
    # ISO形式に従っているかのバリデーション
    date.fromisoformat(s)
    return s


def default_date() -> str:
    tz = timezone(timedelta(hours=9))
    return datetime.now(tz=tz).date().isoformat()


def main():
    # ArgumentParserオブジェクトの作成
    parser = argparse.ArgumentParser(description="コマンドラインツールの例")
    parser.add_argument(
        "command",
        choices=[
            create.__name__,
            delete.__name__,
        ],
    )
    parser.add_argument(
        "--from-date",
        type=date_isoformat,
        # デフォルトは実行日
        default=default_date(),
    )
    parser.add_argument(
        "--to-date",
        type=date_isoformat,
        # デフォルトは実行日
        default=default_date(),
    )

    # 引数を解析
    args = parser.parse_args()

    # サブコマンドに応じた処理
    if args.command == create.__name__:
        create(from_date=args.from_date, to_date=args.to_date)
    elif args.command == delete.__name__:
        delete(from_date=args.from_date, to_date=args.to_date)
    else:
        print("未定義のコマンドです")


if __name__ == "__main__":
    main()
