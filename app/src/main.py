# from .prompt import Prompt
from const import Part, Skills, SHEET_NAME
from prompt import Prompt


def main(model, file_path):
    # response = (model.generate_content(prompt)).text
    # response = '**効果的な AWS 勉強方法**\n\n**1. 公式ドキュメントを活用する**\n* AWS ドキュメントは、包括的で信頼できるリソースです。\n* ドキュメントを検索して、特定のサービスやコンセプトについて学ぶことができます。\n* チュートリアル、リファレンス資料、ベストプラクティスを提供しています。\n\n**2. オンラインコースを受講する**\n* AWS は、初心者から上級者向けの無料および有料のオンラインコースを提供しています。\n* コースは、ガイド付き学習、クイズ、実習を提供し、実践的なスキルを向上させるのに役立ちます。\n* AWS トレーニングおよび認定 Web サイトをご覧ください。\n\n**3. ハンズオンラボを試す**\n* AWS ハンズオンラボは、サービスを実際操作して実験できるインタラクティブなプラットフォームです。\n* ラボはガイド付き手順を提供し、実践的な経験を積みながら学ぶことができます。\n\n**4. AWS ブログとホワイトペーパーを読む**\n* AWS ブログには、業界のトレンド、製品アップデート、ベストプラクティスの洞察が含まれています。\n* ホワイトペーパーは、特定のトピックに関する詳細な技術情報を提供します。\n\n**5. コミュニティに参加する**\n* AWS コミュニティフォーラム、Stack Overflow、LinkedIn グループに参加しましょう。\n* 他の人から学び、質問をして、問題を解決できます。\n\n**6. プロジェクトに取り組む**\n* 実際に AWS を使用したプロジェクトに取り組むと、スキルを固められます。\n* アイデアを得るために、AWS ソリューションアーキテクトのサンプルアーキテクチャを参照してください。\n\n**7. 認定を受ける**\n* AWS 認定は、スキルと知識を検証する貴重な方法です。\n* 認定試験の準備には、コース、実習、認定ガイドを使用してください。\n\n**追加のヒント:**\n\n* **スケジューリングを立てる:** 勉強時間を取り、それに固執します。\n* **一貫した学習:** 少量ずつでも毎日学ぶと、情報が定着しやすくなります。\n* **アクティブラーニング:** ただ読むだけではなく、クイズを解いたり、ラボを実行したりしてアクティブに学習します。\n* **目的を設定する:** 何を学びたいのか、なぜ学ぶのかを特定します。\n* **サポートを求める:** わからないことがあれば、コミュニティや AWS サポートにお問い合わせください。'
    prompts = {
            Part.CERTIFICATION.value: [],
            Part.INTRODUCTION.value: [],
            Part.PROJECT.value: [],
            Part.SKILL.value: [],
        }

    obj = Prompt(file_path)
    read_range = obj.get_info()
    file_index = obj.find_index(read_range)
    for part, range in list(file_index.items()):
        content = obj.get_range_content(part, range)
        prompts[part] = content


    # while True:
    #     try:
    #         _, end = (re.search(r"\n", response)).regs[0]
    #     except AttributeError:
    #         ret.append(response[:])
    #         break
        
    #     ret.append(response[:end])
    #     response = response[end:]
    return prompts


if __name__ == "__main__":
    file_path = '/Users/jun/solution/gemini_app/app/upload/スキルシート(JU).xlsx'
    main("dummy1", file_path)