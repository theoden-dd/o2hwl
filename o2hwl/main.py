#!/usr/bin/env python3
import sys

from obsidian_to_hugo import ObsidianToHugo


def whitelist_file(file_contents: str, file_path: str) -> bool:
    if '#al10' in file_contents:
        return True  # copy file
    else:
        return False  # skip file


# Probably it was simpler to fork.
if __name__ == '__main__':
    print(sys.argv)
    obsidian_to_hugo = ObsidianToHugo(
        obsidian_vault_dir=sys.argv[1],
        hugo_content_dir=sys.argv[2],
        filters=[whitelist_file],
    )

    obsidian_to_hugo.run()
