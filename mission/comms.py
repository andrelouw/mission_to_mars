import sys

# Colored printing functions for strings that use universal ANSI escape sequences.
# fail: bold red, pass: bold green, warn: bold yellow,
# info: bold blue, bold: bold white


class MissionComms:

    @staticmethod
    def print_fail(message):
        sys.stderr.write('\x1b[1;31m' + message.strip() + '\x1b[0m\n')

    @staticmethod
    def print_pass(message):
        sys.stdout.write('\x1b[1;32m' + message.strip() + '\x1b[0m\n')

    @staticmethod
    def print_warn(message):
        sys.stderr.write('\x1b[1;33m' + message.strip() + '\x1b[0m\n')

    @staticmethod
    def print_info(message):
        sys.stdout.write('\x1b[1;34m' + message.strip() + '\x1b[0m\n')

    @staticmethod
    def print_bold(message):
        sys.stdout.write('\x1b[1;37m' + message.strip() + '\x1b[0m\n')