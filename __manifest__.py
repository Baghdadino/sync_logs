{
    'name': "SyncLogs",
    'version': '1.0',
    'depends': ['base', 'smile_audit'],
    'author': "inherit Audit log",
    'category': 'Category',
    'description': """
    Description text
    """,
    # data files always loaded at installation
    'data': [
        # 'security/ir.model.access.csv',
        'views/sync_logs.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        # 'demo/demo_data.xml',
    ],
}