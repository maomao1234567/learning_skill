def get_bin_from_user():
    bin_string = input('请输入一个二进制数：')
    while True:
        is_valid_bin = True
        for bin_number in bin_string:
            if bin_number not in ['0', '1']:
                is_valid_bin = False
        if is_valid_bin:
            return bin_string
        else:
            bin_string = input('请重新输入一个二进制数：')


def main():
    bin_from_user = get_bin_from_user()
    dec_from_bin = int(bin_from_user, 2)
    print(f'你输入的二进制数{bin_from_user}转换为十进制数为{dec_from_bin}')


if __name__ == '__main__':
    main()
