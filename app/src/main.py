import re
import openpyxl
import pandas as pd
from .const import Part


def main(model, file_path):
    # response = (model.generate_content(prompt)).text
    # response = '**効果的な AWS 勉強方法**\n\n**1. 公式ドキュメントを活用する**\n* AWS ドキュメントは、包括的で信頼できるリソースです。\n* ドキュメントを検索して、特定のサービスやコンセプトについて学ぶことができます。\n* チュートリアル、リファレンス資料、ベストプラクティスを提供しています。\n\n**2. オンラインコースを受講する**\n* AWS は、初心者から上級者向けの無料および有料のオンラインコースを提供しています。\n* コースは、ガイド付き学習、クイズ、実習を提供し、実践的なスキルを向上させるのに役立ちます。\n* AWS トレーニングおよび認定 Web サイトをご覧ください。\n\n**3. ハンズオンラボを試す**\n* AWS ハンズオンラボは、サービスを実際操作して実験できるインタラクティブなプラットフォームです。\n* ラボはガイド付き手順を提供し、実践的な経験を積みながら学ぶことができます。\n\n**4. AWS ブログとホワイトペーパーを読む**\n* AWS ブログには、業界のトレンド、製品アップデート、ベストプラクティスの洞察が含まれています。\n* ホワイトペーパーは、特定のトピックに関する詳細な技術情報を提供します。\n\n**5. コミュニティに参加する**\n* AWS コミュニティフォーラム、Stack Overflow、LinkedIn グループに参加しましょう。\n* 他の人から学び、質問をして、問題を解決できます。\n\n**6. プロジェクトに取り組む**\n* 実際に AWS を使用したプロジェクトに取り組むと、スキルを固められます。\n* アイデアを得るために、AWS ソリューションアーキテクトのサンプルアーキテクチャを参照してください。\n\n**7. 認定を受ける**\n* AWS 認定は、スキルと知識を検証する貴重な方法です。\n* 認定試験の準備には、コース、実習、認定ガイドを使用してください。\n\n**追加のヒント:**\n\n* **スケジューリングを立てる:** 勉強時間を取り、それに固執します。\n* **一貫した学習:** 少量ずつでも毎日学ぶと、情報が定着しやすくなります。\n* **アクティブラーニング:** ただ読むだけではなく、クイズを解いたり、ラボを実行したりしてアクティブに学習します。\n* **目的を設定する:** 何を学びたいのか、なぜ学ぶのかを特定します。\n* **サポートを求める:** わからないことがあれば、コミュニティや AWS サポートにお問い合わせください。'

    file_index = get_file_index(file_path)


    ret =[]
    # while True:
    #     try:
    #         _, end = (re.search(r"\n", response)).regs[0]
    #     except AttributeError:
    #         ret.append(response[:])
    #         break
        
    #     ret.append(response[:end])
    #     response = response[end:]
    return ret


def get_file_index(file_path):
    file_index = {
        Part.CERTIFICATION.value: [],
        Part.PROJECT.value: [],
        Part.SKILL.value: [],
    }

    wb = openpyxl.load_workbook(file_path)
    sheet = wb["スキルシート（開発系）"]
    read_range = sheet['B5':'B144']
    file_index = find_dict_name(file_index, read_range)
    return


def find_dict_name(file_index, read_range):
    index_name = list([name for name in list(file_index.keys())])
    start, end = 0, 0

    for idx, row in enumerate(read_range):
        val = row[0].value
        if (val in index_name) or (idx == len(read_range)):
            if start != 0:
                end = idx
                file_index[val] = [start, end]
            start = idx
    return file_index


if __name__ == "__main__":
    main("dummy1", "dummy2")