def main():
    def horse2(position):
        letters = 'abcdefgh'
        numbers = '12345678'

        col = position[0]
        row = int(position[1])

        result = []

        for i in range(-2, 3):
            for j in range(-2, 3):
                if abs(i * j) == 2:
                    new_col = letters.find(col) + i
                    new_row = row + j

                    if 0 <= new_col < len(letters) and 0 < new_row <= len(numbers):
                        result.append(letters[new_col] + str(new_row))

        return result

    position = input()
    possible_moves = horse2(position)
    print(f'Возможные ходы коня из позиции {position}: {possible_moves}')


if __name__ == "__main__":
    main()
