import os
from PIL import Image
import imagehash
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from mlxtend.plotting import plot_confusion_matrix 

#400
# storage={'ac64b531d199c69d': 'Covid (210).png', 
# '9a96e069d149e579': 'Covid (355).png', 
# '8e96e558d04ed1ce': 'Covid (91).png', 
# '8b69f529e08ec2c7': 'Covid (139).png', 
# '9e1cf468c3c2c70f': 'Covid (247).png', 
# '8ec7f700b119965e': 'Covid (302).png', 
# '9b6bb425c48cd29e': 'Covid (181).png', '9ad3e535915c9626': 'Covid (29).png', '9f1cf06843c3c70f': 'Covid (250).png', 'fb64e433c498c59c': 'Covid (314).png', 'bc64b411939bc69e': 'Covid (197).png', '9b62a435c68dd39a': 'Covid (178).png', 'ac73f531d3ccc08c': 'Covid (206).png', 'f904e43396cd96d8': 'Covid (343).png', '9e12e569d0e493c7': 'Covid (87).png', '8a33f53dd1cc90c3': 'Covid (68).png', '8966fc39d1cd80d9': 'Covid (338).png', 'cac2b429c53c9377': 'Covid (292).png', '9b50f543c61e162f': 'Covid (154).png', 'ae33f53cd2ccd088': 'Covid (13).png', '9b46f469c46dc784': 'Covid (380).png', '8b71fd20e764f038': 'Covid (44).png', '9f4ee869c569c0a5': 'Covid (3).png', '8c35f531d1ccd0cb': 'Covid (103).png', 'db46a86bc46986cd': 'Covid (379).png', '8e76e538d18cd0cd': 'Covid (396).png', '8c91f534c1ce92cf': 'Covid (115).png', '9ad2fd218104d7e7': 'Covid (52).png', '8e75f43191ccc0cf': 'Covid (400).png', '9b92e13994cdc749': 'Covid (284).png', '9b018507c61e577f': 'Covid (142).png', '8b69f401c6ced297': 'Covid (134).png', 'ad30f55991cc96c3': 'Covid (72).png', 'da96bd61c149e11d': 'Covid (359).png', '8ad3fd35c50c92c6': 'Covid (25).png', '9a16f469c16dc3a5': 'Covid (162).png', '8966f531d28cd09f': 'Covid (174).png', '9a1bd53cb1ccc287': 'Covid (33).png', 'db64e873a4c8e16c': 'Covid (318).png', '9bd2f43db148c325': 'Covid (64).png', '8e93ed70d48cc34e': 'Covid (123).png', '9b50f561c60fd22e': 'Covid (158).png', 'c8961d71d46ac33e': 'Covid (334).png', '9b61f531e42da26c': 'Covid (271).png', '9a71f520836cf29e': 'Covid (48).png', 'adc6f531911d961a': 'Covid (363).png', '9b69b033c49ec69c': 'Covid (226).png', '8c91f574c14ec34f': 'Covid (119).png', '9b46f963e461946c': 'Covid (375).png', '9b4bb421e19cc7a6': 'Covid (230).png', 'db60e873e46ce14c': 'Covid (322).png', '9b82b539c64dc70d': 'Covid (288).png', '9b64e521e68cd267': 'Covid (267).png', '9972f561c44cd38e': 'Covid (323).png', 'db86a0398749d72d': 'Covid (289).png', '8b64f432c68ed24f': 'Covid (266).png', 'a946f431c6cd939c': 'Covid (374).png', '9b4bd421c19cc7b6': 'Covid (231).png', '8e11f574c14cd34f': 'Covid (118).png', 'cb47e469b1698599': 'Covid (362).png', '9b69b531c58ec694': 'Covid (227).png', '8a58fd30d16cf037': 'Covid (49).png', 'bbe6a423939986ca': 'Covid (335).png', '9b69e131e40da36d': 'Covid (270).png', '9b50d421c60fd3ee': 'Covid (159).png', 'cac2f53da548d23c': 'Covid (65).png', '8c91f570d48ec34f': 'Covid (122).png', '9b64e173c48dd19c': 'Covid (319).png', 'b962e433d28dc09f': 'Covid (175).png', '8e59f534d1ccd286': 'Covid (32).png', '8a51f535916cd2c7': 'Covid (24).png', '9ad2f561c06cd23e': 'Covid (163).png', 'da96bd61c149e14d': 'Covid (358).png', 'cb32e5b3d1cc90c3': 'Covid (73).png', '9b41e503c61e533f': 'Covid (143).png', '9b92f439d0c6c36c': 'Covid (285).png', '8c11f534d1ce92cf': 'Covid (114).png', '8ad3f565c10cd2c7': 'Covid (53).png', '9b4ee069c4edc694': 'Covid (378).png', '8c76e431f18cd0dd': 'Covid (397).png', 'db79a521a76ce430': 'Covid (45).png', '9b4ce86187c9c3b6': 'Covid (2).png', '8d75e511d1ccd0cb': 'Covid (102).png', '9bc6f569c46d8684': 'Covid (381).png', '9b50f543c70e962e': 'Covid (155).png', 'bb33e432d3cc818b': 'Covid (12).png', '9b6cf439915cc4d8': 'Covid (339).png', 'cbc6b425c51d9365': 'Covid (293).png', '9e96ed79c144c1c6': 'Covid (86).png', 'c936e715d1cc94c3': 'Covid (69).png', 'ac66f510d2cbc29b': 'Covid (207).png', 'fb2ce07396cc96c0': 'Covid (342).png', '9d12dc6bf12d9434': 'Covid (196).png', '9d6be535c684c49c': 'Covid (179).png', 'db04a133859997dd': 'Covid (315).png', '9b6bb436c484d29e': 'Covid (180).png', '9a93e52db16c96a4': 'Covid (28).png', '8e1ff568d0c2e10f': 'Covid (246).png', '8d27e744919992db': 'Covid (303).png', '8e96e508d04e93ef': 'Covid (90).png', '8f69f529c28ec2c6': 'Covid (138).png', 'bd64b05195c9c69b': 'Covid (211).png', '9a16e569d56ce065': 'Covid (354).png', '8a33f53ed1cc90c3': 'Covid (74).png', '8ae8e551e5ce920f': 'Covid (133).png', '9b52d461c16dd32d': 'Covid (164).png', '8b71f534856cd2d2': 'Covid (23).png', '8964e433d1ccd3cd': 'Covid (308).png', '9bc3f435c5c2c30e': 'Covid (35).png', '9b66e51196ccd09b': 'Covid (172).png', '9e93e96091cdc746': 'Covid (125).png', '9bd2f43d9148c365': 'Covid (62).png', '8b0ef471c46cf2b8': 'Covid (349).png', '9b33e436c6cc9398': 'Covid (19).png', 'd9861947943bc63e': 'Covid (298).png', 'c8969d71c568d16e': 'Covid (332).png', '9b52f561c42dd24d': 'Covid (277).png', '9e9ee4a952a146b5': 'Covid (9).png', '8c15f534d3ccd0cb': 'Covid (109).png', 'db46e4298799879a': 'Covid (365).png', '9f63f433c28cc09b': 'Covid (220).png', '9a92ed65d14cc627': 'Covid (58).png', '8b4ef439c2edc384': 'Covid (373).png', '9b1ab469e1bdc134': 'Covid (236).png', '9b41d512c60f5b3e': 'Covid (148).png', 'db00e147c497c78f': 'Covid (324).png', '886cf531f22cd267': 'Covid (261).png', '8c67b531f1ccc09d': 'Covid (216).png', '9b16e56dd464c2cc': 'Covid (353).png', 'e939e47c91cc94c3': 'Covid (97).png', '8b33e53ed3cc90c1': 'Covid (77).png', '99d25d3df0cdc061': 'Covid (241).png', '89a6ec1191adc1df': 'Covid (304).png', '9a5bf465c19cc2a6': 'Covid (187).png', 'dbc69471e149d361': 'Covid (168).png', '9b64e433c64dc2ce': 'Covid (257).png', 'db64e433c499c596': 'Covid (312).png', '9bd2a461c5cdc666': 'Covid (191).png', '8a33f576d6ccb018': 'Covid (39).png', '8c77f550d1ccc28b': 'Covid (200).png', '8b2cf57196cc925c': 'Covid (345).png', '8b13f574d5c690c6': 'Covid (81).png', '9f91443e03cd4e3b': 'Covid (128).png', 'cb863507851fd65c': 'Covid (294).png', 'ab33e574828cd1d9': 'Covid (15).png', '9b40e507c71e563e': 'Covid (152).png', 'db46ec61868dc5c9': 'Covid (369).png', '9a96ac69e0cdc761': 'Covid (386).png', '8c35f57cd1ccd4c0': 'Covid (105).png', 'bb73b520c66cf230': 'Covid (42).png', '9e1ee069c1a9c7e1': 'Covid (5).png', 'da869de5f5699201': 'Covid (390).png', '9a92f569c10cd6c7': 'Covid (54).png', '8c11f534c1ced2cf': 'Covid (113).png', '9ab6e569c00cc76d': 'Covid (282).png', '9892e561c5ce872f': 'Covid (328).png', '8979f501d28e52b7': 'Covid (144).png', '8b51f503c60f133f': 'Covid (145).png', '9b92e521f407c747': 'Covid (283).png', 'd9921469c2cf933d': 'Covid (329).png', '9a92f56dc10c96d5': 'Covid (55).png', '8d11e534c50ed3cf': 'Covid (112).png', 'ca8a9de5f469d221': 'Covid (391).png', 'c935e51583dc91ce': 'Covid (104).png', '8b73f520c66cf238': 'Covid (43).png', '9a4ee14bc5e984ad': 'Covid (4).png', '8b66fc61b0cdc4e1': 'Covid (368).png', 'db96bc61c0c9872d': 'Covid (387).png', 'bb33e53092ccd1c9': 'Covid (14).png', '9b50f541c51f960f': 'Covid (153).png', 'cac6bd49c43dc358': 'Covid (295).png', '8b13f574c6ce92c2': 'Covid (80).png', 'ac66f53191ccc49b': 'Covid (201).png', '8b2cf53196cc91dc': 'Covid (344).png', '9bd2a06785c6c69e': 'Covid (190).png', '8a33f57492ece039': 'Covid (38).png', '9b64e433d34cc28f': 'Covid (256).png', '9964e433c6ccd70d': 'Covid (313).png', '9b5bb461c184c7a7': 'Covid (186).png', 'd9c69479e10dd235': 'Covid (169).png', '9996ca6bc4c98735': 'Covid (240).png', '8964ec78916d91db': 'Covid (305).png', '9e16e56a106e173b': 'Covid (96).png', '8b1be57cd6cc94c0': 'Covid (79).png', '9f66a473d48dd085': 'Covid (217).png', '9b1ee969c468e54c': 'Covid (352).png', '9932ed61e54cc5cc': 'Covid (325).png', '9964e531e24dd267': 'Covid (260).png', '9b51f502c60f523f': 'Covid (149).png', '8b66f431c2cdc78c': 'Covid (372).png', '9bd2b461e48dc267': 'Covid (237).png', '9a92ed65c141966f': 'Covid (59).png', 'ed46e46191e9c58d': 'Covid (364).png', '9b6ba433c68dc1c9': 'Covid (221).png', '9f96f42dd0a1c2b1': 'Covid (8).png', '8c15f536d1ce92ca': 'Covid (108).png', 'd9c61a45943bc53d': 'Covid (299).png', 'c8969d71f568d02e': 'Covid (333).png', '8bf2f561e408964f': 'Covid (276).png', '8e31f536d0ce929c': 'Covid (18).png', '9b6ee471c46c9698': 'Covid (348).png', '9e93e960954dc34e': 'Covid (124).png', '9ad2fc3d9148c365': 'Covid (63).png', '9ad3f435d14cc345': 'Covid (34).png', '9b66ad33908dd187': 'Covid (173).png', '8966ec33e1ccd1cc': 'Covid (309).png', '9b84a461c55d973d': 'Covid (165).png', 'db71ac2585ccd0da': 'Covid (22).png', '8b32f53e93cc94c1': 'Covid (75).png', '9968e403d38edb33': 'Covid (132).png', '8a74f532c60dc2cf': 'Covid (263).png', '9912e569c5ccc6ce': 'Covid (326).png', '9b9a9461c19dc7a6': 'Covid (234).png', '8b46f463c6cd82ce': 'Covid (371).png', '9b6bb531c68cc1d8': 'Covid (222).png', 'da96bc69c4c9c325': 'Covid (388).png', '8f46f46990c5c4ed': 'Covid (367).png', '9b72f521e46c9265': 'Covid (275).png', 'c9921469c2cfc36f': 'Covid (330).png', '9a92fd71f149d224': 'Covid (60).png', '9e91ed32d14d920f': 'Covid (127).png', '8964e531f36cd247': 'Covid (259).png', 'd9c6bc71e14dd025': 'Covid (170).png', '8a73f531d3ccd098': 'Covid (37).png', '8a71f534c2ced29a': 'Covid (21).png', '9a96e469411d52bf': 'Covid (166).png', '9adba465c59cc686': 'Covid (189).png', '9e66f511c28cca9e': 'Covid (218).png', '98d1ed12c146d36f': 'Covid (131).png', '8a32e53fd3cc90d1': 'Covid (76).png', '8c34f575d1ccd0c9': 'Covid (99).png', '9b61e511c48f969e': 'Covid (146).png', '9ad2f561c44ec2cd': 'Covid (280).png', '8c11f574d3ccd2c9': 'Covid (111).png', '9a92e565c14dc6c7': 'Covid (56).png', '9992f06be1adc562': 'Covid (238).png', 'da8e39a5b449d2e1': 'Covid (392).png', 'fb23e067c444b32d': 'Covid (40).png', '9e96f569d0a0c2b9': 'Covid (7).png', '8c30f53cd3ced0cc': 'Covid (107).png', '9a86e069c1cf876d': 'Covid (384).png', '8d51f502c28f52bf': 'Covid (150).png', 'af31f536c28c92cc': 'Covid (17).png', '9a92e123e179a36d': 'Covid (279).png', 'c986154f963fc278': 'Covid (296).png', '9b13e575c5c490c7': 'Covid (83).png', '8b2ef571c46cb238': 'Covid (347).png', 'ac66f531d1ccc499': 'Covid (202).png', '9912bc6de1bdc225': 'Covid (193).png', '8964ec33e57cd14c': 'Covid (310).png', '8b74e430d34fc28f': 'Covid (255).png', '9b5ab061c19cc7a7': 'Covid (185).png', '8964e433914dd3cf': 'Covid (306).png', '8f1ef060c3c993c7': 'Covid (243).png', '9e16c16b126e333b': 'Covid (95).png', 'db04e165c64c96de': 'Covid (351).png', '8c66bd7191ccc49b': 'Covid (214).png', '9b5cf465c6c4c296': 'Covid (350).png', 'ac66b531d1ccc29d': 'Covid (215).png', '9e97e560d04e516b': 'Covid (94).png', '9964e433b14cd3cd': 'Covid (307).png', '9a3cf041c7ca96c7': 'Covid (242).png', '9b5ab861e18cc7a5': 'Covid (184).png', 'd964e433c5d9914d': 'Covid (311).png', 
# '9b64e431934ec69e': 'Covid (254).png', '9b92b461e19dc2a7': 'Covid (192).png', 'db2cf471866cb548': 'Covid (346).png', 'ab66f43191cc90db': 'Covid (203).png', '8b13f575c5c4d0c6': 'Covid (82).png', '9b52e163c52d964d': 'Covid (278).png', 'c186156f963dc33c': 'Covid (297).png', '8b59f521c68dd296': 'Covid (151).png', 'af33f534c08c92d9': 'Covid (16).png', '9a86ec69e049c76d': 'Covid (385).png', 'bb31f560c66cf230': 'Covid (41).png', '9e96f469c0adc3e0': 'Covid (6).png', '8c30f57cd3ccd4c1': 'Covid (106).png', '9994da7be0c8943d': 'Covid (239).png', 'da1e3aa7b449b063': 'Covid (393).png', '8c11f574d3ccd2c3': 'Covid (110).png', '9a92fd61d16c8267': 'Covid (57).png', '9ab6ed71ed00e1c8': 'Covid (281).png', '8b69f510c68f5297': 'Covid (147).png', '9e91ec32c14cd36b': 'Covid (130).png', 'ccb1ef55d18c8097': 'Covid (98).png', '9b62a433d28dc89f': 'Covid (219).png', '8b33f534d6cc9298': 'Covid (20).png', '9a86857b473e1e38': 'Covid (167).png', '9adbb465c194c786': 'Covid (188).png', 'c9c69431e52dc33b': 'Covid (171).png', '9bd3f435c1c2c30e': 'Covid (36).png', 'a964e431f34dc2c7': 'Covid (258).png', '9a92f52d914dc347': 'Covid (61).png', '9e13c16e174f4a3a': 'Covid (126).png', '9b70f521e46d926c': 'Covid (274).png', 'd8963c61c5c1c3cf': 'Covid (331).png', '9b69b533e484e4cc': 'Covid (223).png', 'db96bc61c4c9c325': 'Covid (389).png', '8f46f439929d921b': 'Covid (366).png', '9b92bc63e089c727': 'Covid (235).png', '8b46f471d0cdc5c5': 'Covid (370).png', 'bb64e513c689d24e': 'Covid (262).png', '9912c569c1cec66f': 'Covid (327).png', '8d69f529d286d2c6': 'Covid (140).png', '8a65f530e40df26e': 'Covid (269).png', '9b12543bc64e5b3c': 'Covid (286).png', '9b52fc21c56ce626': 'Covid (50).png', '8c11f574d1ccd2c7': 'Covid (117).png', 'd31e29a5b5c1c64b': 'Covid (394).png', '8c39f53cd1ccd4c1': 'Covid (101).png', '9b79e42487ece4b0': 'Covid (46).png', 'd834e41193cdd39b': 'Covid (1).png', '8bc2f461c46dc3d6': 'Covid (382).png', '9b4ab069e594c7a5': 'Covid (228).png', '9e86f5ad70bc42b0': 'Covid (11).png', '9b50f543c60f92ae': 'Covid (156).png', 'db86b1398559126f': 'Covid (290).png', '8a12f56dd1c6d0c7': 'Covid (85).png', 'db2ce03396cc95e8': 'Covid (341).png', '8a66fd71d1cc90c5': 'Covid (204).png', '9d1ad565f1acc072': 'Covid (195).png', 'f904e133c4d9979c': 'Covid (316).png', 'ad74e420938fc68f': 'Covid (253).png', '9b4bb563c5c4c686': 'Covid (183).png', '91c3543943de1be3': 'Covid (300).png', '8e3cf569c0d2874b': 'Covid (245).png', '9e96e561d0ccd163': 'Covid (93).png', 'd8963f61c145e14f': 'Covid (357).png', 'ac64f531d0cdc29e': 'Covid (212).png', '9b64e433c6cec60e': 'Covid (265).png', '9944f573c48c93ce': 'Covid (320).png', '8c76e531f18cd0cd': 'Covid (398).png', '9adab461e19cc6a6': 'Covid (232).png', '9b4ef069c66d86c4': 'Covid (377).png', '9a69f532c68ec09e': 'Covid (224).png', 'ce46e5a99139929e': 'Covid (361).png', '9b70f521e46c92ce': 'Covid (273).png', '8866e439919dc2df': 'Covid (336).png', 'ac64b431939bc49f': 'Covid (208).png', '9993e835c586c74e': 'Covid (121).png', 'c8c2fc3fa5ccd038': 'Covid (66).png', '9e94e978c14cb1c7': 'Covid (89).png', '9bd3f435c1ccc306': 'Covid (31).png', 'bb62a433d28dc19b': 'Covid (176).png', 'ac76f530d1ccc28b': 'Covid (199).png', '9e34f069c3c2c70f': 'Covid (249).png', '9a84c54bc71ed63c': 'Covid (160).png', '9a13e52db16d16b4': 'Covid (27).png', 'c936e71791cc94c3': 'Covid (70).png', '8d69f529e28ec2c6': 'Covid (137).png', 'cb36e51391cc96c3': 'Covid (71).png', '8b69f521c68ed287': 'Covid (136).png', '9952c461c62fd72e': 'Covid (161).png', '9a53e53db12c92a6': 'Covid (26).png', '8e1ff46c50e2e14b': 'Covid (248).png', '9a1bf535f14cd224': 'Covid (30).png', '9962e535c28dc5d9': 'Covid (177).png', '8c66f711d1ccc28f': 'Covid (198).png', '8d1bd16442ce4aef': 'Covid (120).png', 'aa3af53d90cc94c3': 'Covid (67).png', '9e96e141c12dd34f': 'Covid (88).png', '8c66bd31b199c49d': 'Covid (209).png', '9b69f131e44da26c': 'Covid (272).png', 'fb64e4339388c6d8': 'Covid (337).png', '9b6bb433c48cc69c': 'Covid (225).png', 'ee66c18993b31396': 'Covid (360).png', '8e73e431b1ccc18f': 'Covid (399).png', '9adab461e19cc726': 'Covid (233).png', '9b4ef061c46dc6cc': 'Covid (376).png', '9b64f432c69ec22e': 'Covid (264).png', '9b60fd71e56cb044': 'Covid (321).png', '9896bf69c0cd45c5': 'Covid (356).png', '8c66bd7191ccd4c9': 'Covid (213).png', '9e96e569d0ec44e1': 'Covid (92).png', '91c3543b435e1be3': 'Covid (301).png', '8a3cfd61d0ca86cb': 'Covid (244).png', '9b6bbd61c5c4b086': 'Covid (182).png', '9b64f533c4c9d14c': 'Covid (317).png', '8dc3f500938fd28f': 'Covid (252).png', '9912b465e1adc575': 'Covid (194).png', 'db64e431c7ccc4d8': 'Covid (340).png', 'bb66e47193cc90cc': 'Covid (205).png', '8a13f53dc5c690c7': 'Covid (84).png', 'c9c2942dc63c52ef': 'Covid (291).png', '9e96f569d0a8c239': 'Covid (10).png', '9b10e543c51fd62e': 'Covid (157).png', '9a86fd69c469c784': 'Covid (383).png', '9a4bf561e590c786': 'Covid (229).png', '8c34f57cd1ce90c9': 'Covid (100).png', '9a79f524c3ccd292': 'Covid (47).png', '8f74e431918cd19f': 'Covid (395).png', '8ad3fd21c564f207': 'Covid (51).png', '8e11f534d1dc92c7': 'Covid (116).png', '9a65ed21e48de067': 'Covid (268).png', '9bd2f439964cc34c': 'Covid (287).png', '8d6cf521d28ed287': 'Covid (141).png'}

#3871
storage={}


#small data
# images='./400storagesim'
# test='./250copystorage'


#big data
images='./originalbig'
test='./bigonefourth'

# for getting orig hashes
def confusionmatrix(hashfunc):
    for filename in os.listdir(images):
        if filename.endswith(".jpeg") or filename.endswith(".png"):
            image_path = os.path.join(images, filename)
            image = Image.open(image_path)
            hash_value = str(hashfunc(image))
            storage[hash_value] = filename


confusionmatrix(imagehash.average_hash)

# for test images
# def confusionmatrix(hashfunc):
#     num = tp = tn = fp = fn = 0
#     for filename in os.listdir(images):
#         num+=1
#         if filename.endswith(".jpeg") or filename.endswith(".png"):
#             image_path = os.path.join(images, filename)
#             image = Image.open(image_path)
#             hash_value = str(hashfunc(image))
#             for hash_values, names in storage.items():
#                 if hash_value==hash_values and filename==names:
#                     tp+=1
#                     continue
#                 if hash_value==hash_values and filename!=names:
#                     tn+=1
#                     continue
#                 if hash_value!=hash_values and filename==names:
#                     fp+=1
#                     continue
#                 if hash_value!=hash_values and filename!=names:
#                     fn+=1
#                     continue
#     print('true_positive %', (tp / num) * 100)
#     print('true_negative %', (tn / num) * 100)
#     print('false_positive %', (fp / num) * 100)
#     print('false_negative %', (fn / num) * 100)    

# confusionmatrix(imagehash.phash)     

    

def confusionmatrix(hashfunc):
    num = tp = tn = fp = fn = 0
    for filename in os.listdir(test):
        if filename.endswith(".jpeg") or filename.endswith(".png"):
            num += 1
            image_path = os.path.join(test, filename)
            image = Image.open(image_path)
            hash_value = str(hashfunc(image))
            if hash_value in storage:
                if filename == storage[hash_value]:
                    tp += 1
                else:
                    fp += 1
            else:
                if any(filename == names for names in storage.values()):
                    tn += 1
                else:
                    fn += 1
    print('true_positive %', (tp / num) * 100)
    print('true_negative %', (tn / num) * 100)
    print('false_positive %', (fp / num) * 100)
    print('false_negative %', (fn / num) * 100)

confusionmatrix(imagehash.average_hash)    



