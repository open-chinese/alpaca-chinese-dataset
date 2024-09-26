import json


def run():
    with open('./alpaca-chinese-52k-v3.json', 'r', encoding='utf-8') as rf:
        samples = json.load(rf)
        score_count = {}
        for s in samples:
            score = s.get('metadata', {}).get('score')
            if score not in score_count:
                score_count[score] = 1
            else:
                score_count[score] += 1

        print(score_count)
        score_dist = {k: round(v / sum(score_count.values()), 2) for k, v in score_count.items()}
        print(score_dist)


if __name__ == '__main__':
    run()