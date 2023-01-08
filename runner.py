all_ids = ['BXD74', 'BXD65b', 'BXD93', 'BXD94', 'A/J', 'AKR/J', 'C3H/HeJ', 'C57BL/6ByJ', 'CXB1', 'CXB2', 'CXB3', 'BXD90', 'BXD89', 'BXD75', 'BXD76', 'BXD77', 'BXD79', 'BXD73a', 'BXD83', 'BXD84', 'BXD85', 'BXD86', 'BXD87', 'CXB4', 'CXB5', 'CXB6', 'LG/J', 'NOD/ShiLtJ', 'PWD/PhJ', 'BXD65a', 'BXD98', 'BXD99', 'CAST/EiJ', 'WSB/EiJ', 'NZO/HlLtJ', 'PWK/PhJ', 'KK/HlJ', 'BALB/cByJ', 'CXB7', 'CXB8', 'CXB9', 'CXB10', 'CXB11', 'CXB12', 'CXB13', 'BXD48a', '129S1/SvImJ', 'BALB/cJ', 'D2B6F1', 'BXD73', 'B6D2F1', 'BXD16', 'BXD19', 'BXD20', 'BXD21', 'BXD22', 'BXD23', 'BXD24', 'BXD27', 'BXD28', 'BXD29', 'BXD15', 'BXD13', 'C57BL/6J', 'DBA/2J', 'BXD1', 'BXD2', 'BXD5', 'BXD6', 'BXD8', 'BXD9', 'BXD11', 'BXD12', 'BXD31', 'BXD32', 'BXD33', 'BXD55', 'BXD60', 'BXD61', 'BXD62', 'BXD63', 'BXD64', 'BXD65', 'BXD66', 'BXD69', 'BXD70', 'BXD51', 'BXD50', 'BXD48', 'BXD34', 'BXD38', 'BXD39', 'BXD40', 'BXD42', 'BXD67', 'BXD68', 'BXD43', 'BXD44', 'BXD45']


target_ids = {'C57BL/6J': 6.638, 'DBA/2J': 6.266, 'B6D2F1': 6.494, 'D2B6F1': 6.565, 'BXD1': 6.357, 'BXD2': 6.456, 'BXD5': 6.59, 'BXD6': 6.568, 'BXD8': 6.581, 'BXD9': 6.322, 'BXD11': 6.519, 'BXD12': 6.543, 'BXD13': 6.636, 'BXD15': 6.578, 'BXD16': 6.636, 'BXD19': 6.562, 'BXD20': 6.61, 'BXD21': 6.668, 'BXD22': 6.607, 'BXD23': 6.513, 'BXD24': 6.601, 'BXD27': 6.573, 'BXD28': 6.639, 'BXD29': 6.656, 'BXD31': 6.549, 'BXD32': 6.502, 'BXD33': 6.584, 'BXD34': 6.261, 'BXD38': 6.646, 'BXD39': 6.584, 'BXD40': 6.79, 'BXD42': 6.536, 'BXD43': 6.476, 'BXD44': 6.545, 'BXD45': 6.742, 'BXD48': 6.393, 'BXD48a': 6.618, 'BXD50': 6.496, 'BXD51': 6.494, 'BXD55': 6.263, 'BXD60': 6.541, 'BXD61': 6.662, 'BXD62': 6.628, 'BXD63': 6.556, 'BXD64': 6.572, 'BXD65': 6.53, 'BXD65a': 6.28, 'BXD65b': 6.49, 'BXD66': 6.608, 'BXD67': 6.534, 'BXD68': 6.352, 'BXD69': 6.548, 'BXD70': 6.52, 'BXD73': 6.484, 'BXD73a': 6.486, 'BXD74': 6.639, 'BXD75': 6.401, 'BXD76': 6.452, 'BXD77': 6.568, 'BXD79': 6.642, 'BXD83': 6.446, 'BXD84': 6.582, 'BXD85': 6.484, 'BXD86': 6.877, 'BXD87': 6.474, 'BXD89': 6.676, 'BXD90': 6.644, 'BXD93': 6.62, 'BXD94': 6.528, 'BXD98': 6.486, 'BXD99': 6.53}



results = []

index = []
for (idx,strain) in enumerate(all_ids):
	if strain in target_ids:
		results.append(strain)
		index.append(idx)

breakpoint()
