#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from pathlib import Path
from typing import Optional

def list_files(path: Path, show_size: bool, only_dir: bool, size: Optional[int] = None) -> None:
    for item in path.iterdir():
        if item.is_file() and not only_dir:
            if show_size:
                size = item.stat().st_size
            print(f"{item.name} {size if size is not None else ''}")
        elif item.is_dir():
            if show_size:
                size = item.stat().st_size
            print(f"{item.name}/ {size if size is not None else ''}")

            list_files(item, show_size, only_dir)

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Утилита для отображения дерева каталогов и файлов"
    )
    parser.add_argument("path", nargs="?", default=".", help="Путь к каталогу")
    parser.add_argument(
        "-d", "--dir", action='store_true', help="Показывать содержимое директории"
    )
    parser.add_argument(
        "-s", "--showsize", action='store_true', help="Показать размер файлов"
    )
    args = parser.parse_args()

    path = Path(args.path)
    only_dir = args.dir
    show_size = args.showsize

    if path.is_dir():
        list_files(path, show_size, only_dir)
    else:
        print(f"Путь {args.path} не существует или не является каталогом")

if __name__ == "__main__":
    main()