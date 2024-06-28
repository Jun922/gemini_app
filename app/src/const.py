from enum import Enum


class Part(Enum):
    CERTIFICATION = "資格"
    INTRODUCTION = "スキル要約\n(自己PR)"
    PROJECT = "No"
    SKILL = "保有技術"


class Skills(Enum):
    SCOPE = "業務範囲"
    OS = "OS"
    LANGUAGE = "言語"
    DB = "データベース"
    FRAME = "各フレームワーク/ライブラリ"
    CLOUD = "クラウドサービス"
    INFRA = "プロジェクト管理系"
    IDE = "開発環境"
    CRM = "CRM"


class Levels(Enum):
    LEVEL_A = "業務の独力遂行、業務課題発見・解決、後進教育ができる"
    LEVEL_B = "業務の独力遂行ができる"
    LEVEL_C = "業務を上位者指導のもと遂行ができる"
    LEVEL_D = "実務を通じた学習経験あり"
    LEVEL_E = "独自学習経験あり"


SHEET_NAME = "スキルシート（開発系）"