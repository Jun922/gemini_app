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


SHEET_NAME = "スキルシート（開発系）"