from collections import defaultdict

def mix_and_prune(secret):
    secret = (secret * 64) ^ secret
    secret %= 16777216
    secret = (secret // 32) ^ secret
    secret %= 16777216
    secret = (secret * 2048) ^ secret
    secret %= 16777216
    return secret

def generate_secret_numbers(initial_secret, count):
    secret = initial_secret
    for _ in range(count):
        secret = mix_and_prune(secret)
    return secret

def main():
    with open('INPUT.TXT', 'r') as file:
        initial_secrets = [int(line.strip()) for line in file.readlines()]

    total = 0
    for secret in initial_secrets:
        total += generate_secret_numbers(secret, 2000)

    print(total)

if __name__ == "__main__":
    main()
    def get_prices(secret, count):
        prices = []
        for _ in range(count):
            secret = mix_and_prune(secret)
            prices.append(secret % 10)
        return prices

    def find_best_sequence(initial_secrets, sequence_length, count):

        sequence_counts = defaultdict(int)
        for secret in initial_secrets:
            prices = get_prices(secret, count)
            for i in range(len(prices) - sequence_length):
                sequence = tuple(prices[i:i + sequence_length])
                sequence_counts[sequence] += 1

        best_sequence = max(sequence_counts, key=sequence_counts.get)
        return best_sequence

    def calculate_bananas(initial_secrets, best_sequence, count):
        total_bananas = 0
        sequence_length = len(best_sequence)

        for secret in initial_secrets:
            prices = get_prices(secret, count)
            for i in range(len(prices) - sequence_length):
                if tuple(prices[i:i + sequence_length]) == best_sequence:
                    total_bananas += prices[i + sequence_length]
                    break

        return total_bananas

    def main():
        with open('INPUT.TXT', 'r') as file:
            initial_secrets = [int(line.strip()) for line in file.readlines()]

        sequence_length = 4
        count = 2000

        best_sequence = find_best_sequence(initial_secrets, sequence_length, count)
        total_bananas = calculate_bananas(initial_secrets, best_sequence, count)

        print(total_bananas)

    if __name__ == "__main__":
        main()