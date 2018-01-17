from toArgv import toArgv
import sys, argparse

LABEL_MAP ={
    3: (4242,4243),
    5: (4244,4245),
    7: (4246,4247,4248,4249),
    11: (4250,4251),
    18: (4252,4253,4254,4255,4256,4257),
    19: (4258,4259,4260),
    28: (4261,4262,4263,4264,4265),
    29: (4266,4267),
    34: (4268,4269),
    45: (4270,4271),
    46: (4272,4273,4274),
    47: (4275,4276),
    52: (4277,4278),
    58: (4279,4280,4281,4282),
    63: (4283,4284),
    89: (4285,4286),
    95: (4287,4288),
    101: (4289,4290),
    104: (4291,4292),
    106: (4293,4294),
    108: (4295,4296,4297),
    119: (4298,4299),
    120: (4300,4301,4302,4303),
    142: (4304,4305),
    160: (4306,4307),
    161: (4308,4309),
    162: (4310,4311),
    164: (4312,4313,4314,4315),
    166: (4316,4317,4318),
    174: (4319,4320),
    184: (4321,4322),
    209: (4323,4324),
    215: (4325,4326,4327,4328),
    236: (4329,4330),
    246: (4331,4332,4333,4334),
    250: (4335,4336),
    279: (4337,4338),
    282: (4339,4340),
    283: (4341,4342),
    291: (4343,4344),
    325: (4345,4346,4347),
    335: (4348,4349),
    338: (4350,4351,4352),
    369: (4353,4354),
    370: (4355,4356,4357),
    383: (4358,4359),
    384: (4360,4361),
    389: (4362,4363),
    400: (4364,4365),
    404: (4366,4367),
    410: (4368,4369),
    430: (4370,4371,4372,4373,4374,4375),
    433: (4376,4377),
    436: (4378,4379),
    440: (4380,4381),
    441: (4382,4383),
    450: (4384,4385),
    455: (4386,4387,4388,4389),
    460: (4390,4391),
    469: (4392,4393),
    473: (4394,4395),
    481: (4396,4397),
    495: (4398,4399,4400),
    500: (4401,4402,4403),
    504: (4404,4405,4406),
    512: (4407,4408),
    544: (4409,4410,4411),
    552: (4412,4413),
    555: (4414,4415,4416),
    563: (4417,4418,4419),
    566: (4420,4421,4422),
    572: (4423,4424,4425),
    586: (4426,4427),
    610: (4428,4429),
    613: (4430,4431),
    623: (4432,4433),
    624: (4434,4435),
    625: (4436,4437),
    627: (4438,4439,4440),
    633: (4441,4442,4443),
    639: (4444,4445),
    649: (4446,4447,4448,4449,4450,4451,4452),
    656: (4453,4454),
    657: (4455,4456),
    671: (4457,4458,4459),
    673: (4460,4461),
    695: (4462,4463,4464),
    696: (4465,4466),
    707: (4467,4468),
    713: (4469,4470),
    714: (4471,4472),
    719: (4473,4474),
    720: (4475,4476,4477,4478),
    725: (4479,4480),
    728: (4481,4482),
    741: (4483,4484),
    752: (4485,4486),
    758: (4487,4488),
    767: (4489,4490),
    771: (4491,4492),
    772: (4493,4494),
    775: (4495,4496),
    797: (4497,4498),
    798: (4499,4500),
    799: (4501,4502,4503),
    800: (4504,4505),
    808: (4506,4507),
    827: (4508,4509,4510),
    839: (4511,4512,4513),
    859: (4514,4515),
    866: (4516,4517),
    883: (4518,4519,4520),
    889: (4521,4522,4523),
    893: (4524,4525),
    896: (4526,4527,4528,4529,4530,4531),
    934: (4532,4533,4534),
    943: (4535,4536,4537,4538),
    949: (4539,4540),
    950: (4541,4542),
    962: (4543,4544),
    965: (4545,4546),
    966: (4547,4548,4549),
    977: (4550,4551),
    994: (4552,4553),
    1006: (4554,4555,4556),
    1024: (4557,4558),
    1058: (4559,4560),
    1080: (4561,4562),
    1087: (4563,4564),
    1142: (4565,4566,4567),
    1143: (4568,4569),
    1147: (4570,4571),
    1170: (4572,4573),
    1175: (4574,4575),
    1185: (4576,4577,4578),
    1186: (4579,4580),
    1193: (4581,4582),
    1198: (4583,4584),
    1212: (4585,4586),
    1237: (4587,4588,4589,4590),
    1257: (4591,4592),
    1258: (4593,4594),
    1271: (4595,4596),
    1277: (4597,4598,4599,4600),
    1283: (4601,4602),
    1297: (4603,4604,4605),
    1304: (4606,4607),
    1308: (4608,4609),
    1316: (4610,4611),
    1340: (4612,4613),
    1349: (4614,4615),
    1355: (4616,4617),
    1362: (4618,4619),
    1376: (4620,4621),
    1411: (4622,4623),
    1413: (4624,4625,4626,4627,4628),
    1447: (4629,4630),
    1455: (4631,4632,4633),
    1474: (4634,4635),
    1501: (4636,4637,4638,4639),
    1505: (4640,4641),
    1521: (4642,4643,4644),
    1531: (4645,4646,4647),
    1547: (4648,4649),
    1563: (4650,4651),
    1583: (4652,4653),
    1595: (4654,4655),
    1600: (4656,4657),
    1625: (4658,4659),
    1634: (4660,4661),
    1637: (4662,4663),
    1656: (4664,4665,4666,4667,4668,4669,4670),
    1658: (4671,4672),
    1665: (4673,4674,4675,4676,4677),
    1680: (4678,4679),
    1687: (4680,4681,4682,4683,4684,4685,4686),
    1690: (4687,4688),
    1692: (4689,4690,4691),
    1693: (4692,4693,4694),
    1697: (4695,4696,4697),
    1700: (4698,4699,4700,4701),
    1705: (4702,4703),
    1710: (4704,4705),
    1711: (4706,4707),
    1732: (4708,4709),
    1741: (4710,4711),
    1747: (4712,4713),
    1748: (4714,4715,4716),
    1757: (4717,4718),
    1762: (4719,4720,4721),
    1771: (4722,4723),
    1775: (4724,4725),
    1783: (4726,4727,4728),
    1787: (4729,4730,4731,4732),
    1794: (4733,4734),
    1805: (4735,4736),
    1808: (4737,4738,4739,4740),
    1819: (4741,4742,4743,4744,4745,4746,4747),
    1847: (4748,4749),
    1848: (4750,4751),
    1853: (4752,4753),
    1859: (4754,4755,4756),
    1881: (4757,4758),
    1884: (4759,4760,4761,4762,4763),
    1885: (4764,4765),
    1886: (4766,4767),
    1889: (4768,4769),
    1895: (4770,4771),
    1907: (4772,4773),
    1908: (4774,4775),
    1912: (4776,4777,4778),
    1917: (4779,4780,4781,4782,4783,4784,4785,4786,4787),
    1926: (4788,4789),
    1931: (4790,4791,4792),
    1951: (4793,4794),
    1960: (4795,4796),
    1969: (4797,4798),
    1996: (4799,4800,4801,4802,4803),
    2002: (4804,4805),
    2008: (4806,4807),
    2010: (4808,4809),
    2035: (4810,4811),
    2036: (4812,4813,4814,4815,4816,4817),
    2049: (4818,4819),
    2052: (4820,4821),
    2064: (4822,4823,4824),
    2074: (4825,4826),
    2088: (4827,4828),
    2097: (4829,4830,4831,4832),
    2114: (4833,4834),
    2123: (4835,4836,4837),
    2149: (4838,4839),
    2161: (4840,4841,4842),
    2162: (4843,4844,4845),
    2196: (4846,4847),
    2206: (4848,4849,4850),
    2207: (4851,4852),
    2209: (4853,4854),
    2215: (4855,4856),
    2241: (4857,4858,4859),
    2255: (4860,4861),
    2256: (4862,4863,4864),
    2308: (4865,4866),
    2316: (4867,4868),
    2331: (4869,4870,4871),
    2387: (4872,4873),
    2436: (4874,4875),
    2469: (4876,4877),
    2478: (4878,4879,4880),
    2483: (4881,4882),
    2510: (4883,4884),
    2516: (4885,4886),
    2532: (4887,4888,4889),
    2545: (4890,4891),
    2554: (4892,4893),
    2559: (4894,4895),
    2564: (4896,4897),
    2572: (4898,4899,4900,4901),
    2579: (4902,4903),
    2587: (4904,4905),
    2606: (4906,4907),
    2625: (4908,4909),
    2641: (4910,4911),
    2658: (4912,4913),
    2670: (4914,4915),
    2673: (4916,4917),
    2675: (4918,4919,4920,4921,4922),
    2680: (4923,4924,4925),
    2683: (4926,4927,4928),
    2690: (4929,4930,4931,4932,4933,4934,4935,4936,4937,4938,4939,4940,4941,4942),
    2693: (4943,4944),
    2710: (4945,4946),
    2715: (4947,4948),
    2718: (4949,4950),
    2757: (4951,4952),
    2763: (4953,4954,4955,4956),
    2771: (4957,4958),
    2809: (4959,4960),
    2828: (4961,4962),
    2840: (4963,4964),
    2844: (4965,4966),
    2905: (4967,4968),
    2924: (4969,4970,4971),
    2939: (4972,4973,4974),
    2942: (4975,4976),
    2979: (4977,4978),
    3010: (4979,4980),
    3012: (4981,4982),
    3020: (4983,4984),
    3040: (4985,4986),
    3048: (4987,4988),
    3085: (4989,4990,4991),
    3110: (4992,4993),
    3117: (4994,4995),
    3152: (4996,4997),
    3160: (4998,4999,5000,5001,5002,5003,5004),
    3165: (5005,5006,5007),
    3191: (5008,5009,5010),
    3201: (5011,5012,5013),
    3269: (5014,5015),
    3295: (5016,5017,5018,5019,5020,5021,5022,5023),
    3327: (5024,5025),
    3409: (5026,5027,5028),
    3411: (5029,5030),
    3412: (5031,5032),
    3419: (5033,5034),
    3430: (5035,5036),
    3442: (5037,5038),
    3448: (5039,5040),
    3453: (5041,5042),
    3483: (5043,5044),
    3487: (5045,5046),
    3496: (5047,5048),
    3501: (5049,5050),
    3524: (5051,5052),
    3560: (5053,5054),
    3594: (5055,5056),
    3630: (5057,5058),
    3667: (5059,5060),
    3670: (5061,5062),
    3678: (5063,5064),
    3683: (5065,5066,5067),
    3698: (5068,5069),
    3733: (5070,5071),
    3734: (5072,5073),
    3808: (5074,5075),
    3896: (5076,5077),
    3898: (5078,5079,5080),
    3918: (5081,5082),
    3923: (5083,5084),
    3934: (5085,5086),
    3952: (5087,5088),
    4037: (5089,5090),
    4041: (5091,5092),
    4054: (5093,5094,5095,5096,5097,5098,5099,5100),
    4092: (5101,5102),
    4123: (5103,5104),
    4155: (5105,5106),
    4156: (5107,5108,5109,5110),
    4162: (5111,5112),
    4176: (5113,5114),
    4194: (5115,5116),
    4228: (5117,5118),
    4234: (5119,5120),
}

first_labels = sorted(LABEL_MAP.keys())

URL = "https://dojo.rc.fas.harvard.edu/ng/#!{'layers':{'em':{'type':'image'_'source':'ndstore://https://dojo.rc.fas.harvard.edu/JWR::2018_01_10::konsta_450/em'}_'gt':{'type':'segmentation'_'source':'precomputed://https://dojo.rc.fas.harvard.edu/pre/JWR::2018_01_10::konsta_450/gt'_'selectedAlpha':1_'objectAlpha':1_'segments':[%s]}_'id':{'type':'segmentation'_'source':'precomputed://https://dojo.rc.fas.harvard.edu/pre/JWR::2018_01_10::konsta_450/id'_'selectedAlpha':0.39_'objectAlpha':0.94_'segments':[%s]}}_'navigation':{'pose':{'position':{'voxelSize':[4_4_30]_'voxelCoordinates':[227.84408569335938_1159.0234375_133.25015258789062]}}_'zoomFactor':6.76439449176896}_'perspectiveOrientation':[0.8022819757461548_-0.2906529903411865_0.18861187994480133_-0.4860967695713043]_'perspectiveZoom':188.88551101387154}"

def get_labels(index):
    label_0 = first_labels[index]
    label_n = LABEL_MAP[label_0]
    # Make strings for original and new labels
    iter_n = map("'{}'".format, label_n)
    str_n = '_'.join(iter_n)
    str_0 = "'%d'" % label_0
    # Format the URL
    return (str_0, str_n)

def start(_argv):

    args = parseArgv(_argv)
    INDEX = args['index']
 
    print URL % get_labels(INDEX)

def parseArgv(argv):
    sys.argv = argv

    help = {
        'help': 'Make NG URL for a mapping of IDs',
        'index': 'URL index for ID mapping',
    }

    parser = argparse.ArgumentParser(description=help['help'])
    parser.add_argument('index', type=int, help=help['index'])

    # Get all arguments
    return vars(parser.parse_args())

def main(*_args, **_flags):
    return start(toArgv(*_args, **_flags))

if __name__ == "__main__":
    start(sys.argv)