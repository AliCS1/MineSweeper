import pygame
import random





pygame.init()

length = 1000

width = length
height = length

Screen = pygame.display.set_mode((width,height))

class Board:
    def __init__(self,x,y,TileSize,amountOfbombs):
        self.TotalTiles = x*y
        self.xBlocks = x
        self.yBlocks = y
        self.xCentre = width/2
        self.yCentre = height/2
        self.Tilesize = TileSize
        self.Bombs = amountOfbombs
        self.xStarting = self.xCentre-(0.5*(self.Tilesize*self.xBlocks))
        self.yStarting = self.yCentre-(0.5*(self.Tilesize*self.yBlocks))
        self.BombGenerate()

    def BombGenerate(self):
        self.Bomb = []
        while len(self.Bomb)< self.Bombs:
            BombAlreadyExists = False
            BombPicker = random.randint(0,self.TotalTiles)
            if len(self.Bomb)==0:
                self.Bomb.append(BombPicker)
            else:
                for i in self.Bomb:
                    if i == BombPicker:
                        BombAlreadyExists = True
                if BombAlreadyExists == False:
                    self.Bomb.append(BombPicker)
                else:
                    pass
        print(self.Bomb)
    def ApplyBombs(self):
        for i in self.Bomb:
            Tiles[i].Bomb = True

    def ApplyBombCounter(self):
        for i in self.Bomb:
            if i == 0:
                self.AddBomb(i+1)
                self.AddBomb(i+Board.xBlocks)
                self.AddBomb(i+Board.xBlocks+1)
            elif i == (Board.xBlocks-1):
                self.AddBomb(i-1)
                self.AddBomb(i+Board.xBlocks-1)
                self.AddBomb(i+Board.xBlocks)
            elif i == (Board.TotalTiles-Board.xBlocks-1):
                self.AddBomb(i-Board.xBlocks)
                self.AddBomb(i-Board.xBlocks+1)
                self.AddBomb(i+1)
            elif i == (Board.TotalTiles-1):
                self.AddBomb(i-Board.xBlocks-1)
                self.AddBomb(i-Board.xBlocks)
                self.AddBomb(i-1)
            elif (i%Board.xBlocks) == 0:
                self.AddBomb(i-Board.xBlocks+1)
                self.AddBomb(i-Board.xBlocks)
                self.AddBomb(i+1)
                self.AddBomb(i+Board.xBlocks+1)
                self.AddBomb(i+Board.xBlocks)
            elif (i%Board.xBlocks) == (Board.xBlocks-1):
                self.AddBomb(i-Board.xBlocks-1)
                self.AddBomb(i-Board.xBlocks)
                self.AddBomb(i-1)
                self.AddBomb(i+Board.xBlocks-1)
                self.AddBomb(i+Board.xBlocks)
            elif (i > 0) and (i < Board.xBlocks):
                self.AddBomb(i+1)
                self.AddBomb(i-1)
                self.AddBomb(i+Board.xBlocks-1)
                self.AddBomb(i+Board.xBlocks)
                self.AddBomb(i+Board.xBlocks+1)
            elif (i < Board.TotalTiles) and (i > (Board.TotalTiles-Board.xBlocks)):
                self.AddBomb(i-Board.xBlocks-1)
                self.AddBomb(i-Board.xBlocks)
                self.AddBomb(i-Board.xBlocks+1)
                self.AddBomb(i+1)
                self.AddBomb(i-1)
            else:
                self.AddBomb(i-Board.xBlocks-1)
                self.AddBomb(i-Board.xBlocks)
                self.AddBomb(i-Board.xBlocks+1)
                self.AddBomb(i-1)
                self.AddBomb(i+1)
                self.AddBomb(i+Board.xBlocks-1)
                self.AddBomb(i+Board.xBlocks)
                self.AddBomb(i+Board.xBlocks+1)

    def AddBomb(self,i):
        Tiles[i].NumberOfBombs = Tiles[i].NumberOfBombs + 1

class Tile:
    def __init__(self,position):
        self.TileSize = Board.Tilesize
        self.Position = position
        self.color1 = (255,210,100)
        self.color2 = (230,250,195)
        self.Hidden = True
        self.Bomb = False
        self.Flag = False
        self.NumberOfBombs = 0
    def FindCordOnMap(self):
        self.x = Board.xStarting + self.NumToCords("X",self.Position)*self.TileSize
        self.y = Board.yStarting + self.NumToCords("Y",self.Position)*self.TileSize
        self.XAdjusted = self.NumToCords("X",self.Position)
        self.YAdjusted = self.NumToCords("Y",self.Position)
        self.xCentre = self.x+(0.5*self.TileSize)
        self.yCentre = self.y+(0.5*self.TileSize)
        if (self.XAdjusted+self.YAdjusted)%2 == 0:
            self.color = self.color1
        else:
            self.color = self.color2
    def NumToCords(self,XY,number):
        if XY == "X":
            return (number%Board.xBlocks)
        elif XY == "Y":
            return int(number/(Board.xBlocks))

    def Draw(self):
        pygame.draw.rect(Screen,self.color,(self.x,self.y,self.TileSize,self.TileSize))
        if self.Flag == True:
            pygame.draw.rect(Screen,(5,215,160),(self.x+(0.25*self.TileSize),self.y+(0.25*self.TileSize),0.5*self.TileSize,0.5*self.TileSize))
        if self.Hidden == False:
            if self.Bomb == True:
                pygame.draw.circle(Screen,(255,80,80),(self.xCentre,self.yCentre),10)
            elif self.NumberOfBombs == 0:
                self.BreakSurroundings()
            else:
                self.label = font.render(str(self.NumberOfBombs),3,(255,255,255))
                self.label = pygame.transform.scale(self.label,(self.TileSize,self.TileSize))
                Screen.blit(self.label,(self.x,self.y))
    def BreakSurroundings(self):
        if self.Position == 0:
            self.TileBreaker(self.Position+1)
            self.TileBreaker(self.Position+Board.xBlocks)
            self.TileBreaker(self.Position+Board.xBlocks+1)
        elif self.Position == (Board.xBlocks-1):
            self.TileBreaker(self.Position-1)
            self.TileBreaker(self.Position+Board.xBlocks-1)
            self.TileBreaker(self.Position+Board.xBlocks)
        elif self.Position == (Board.TotalTiles-Board.xBlocks-1):
            self.TileBreaker(self.Position-Board.xBlocks)
            self.TileBreaker(self.Position-Board.xBlocks+1)
            self.TileBreaker(self.Position+1)
        elif self.Position == (Board.TotalTiles-1):
            self.TileBreaker(self.Position-Board.xBlocks-1)
            self.TileBreaker(self.Position-Board.xBlocks)
            self.TileBreaker(self.Position-1)
        elif (self.Position%Board.xBlocks) == 0:
            self.TileBreaker(self.Position-Board.xBlocks+1)
            self.TileBreaker(self.Position-Board.xBlocks)
            self.TileBreaker(self.Position+1)
            self.TileBreaker(self.Position+Board.xBlocks+1)
            self.TileBreaker(self.Position+Board.xBlocks)
        elif (self.Position%Board.xBlocks) == (Board.xBlocks-1):
            self.TileBreaker(self.Position-Board.xBlocks-1)
            self.TileBreaker(self.Position-Board.xBlocks)
            self.TileBreaker(self.Position-1)
            self.TileBreaker(self.Position+Board.xBlocks-1)
            self.TileBreaker(self.Position+Board.xBlocks)
        elif (self.Position > 0) and (self.Position < Board.xBlocks):
            self.TileBreaker(self.Position+1)
            self.TileBreaker(self.Position-1)
            self.TileBreaker(self.Position+Board.xBlocks-1)
            self.TileBreaker(self.Position+Board.xBlocks)
            self.TileBreaker(self.Position+Board.xBlocks+1)
        elif (self.Position < Board.TotalTiles) and (self.Position > (Board.TotalTiles-Board.xBlocks)):
            self.TileBreaker(self.Position-Board.xBlocks-1)
            self.TileBreaker(self.Position-Board.xBlocks)
            self.TileBreaker(self.Position-Board.xBlocks+1)
            self.TileBreaker(self.Position+1)
            self.TileBreaker(self.Position-1)
        else:
            self.TileBreaker(self.Position-Board.xBlocks-1)
            self.TileBreaker(self.Position-Board.xBlocks)
            self.TileBreaker(self.Position-Board.xBlocks+1)
            self.TileBreaker(self.Position-1)
            self.TileBreaker(self.Position+1)
            self.TileBreaker(self.Position+Board.xBlocks-1)
            self.TileBreaker(self.Position+Board.xBlocks)
            self.TileBreaker(self.Position+Board.xBlocks+1)

    def TileBreaker(self,position):
        if Tiles[position].Flag == False:
            Tiles[position].Hidden = False

    def CheckColor(self):
        if self.Hidden == False:
            if self.color == (255,210,100):
                self.color = (205,220,220)
            elif self.color == (230,250,195):
                self.color = (155,210,210)
        

def MouseClick(pos,button):
    for i in range(0,Board.TotalTiles):
        if pos[0]>Tiles[i].x and pos[0]<(Tiles[i].x+Board.Tilesize) and pos[1]>Tiles[i].y and pos[1]<(Tiles[i].y+Board.Tilesize):
            if button == "left" and Tiles[i].Flag != True:
                Tiles[i].Hidden = False
            elif button == "right":
                if Tiles[i].Flag == True and Tiles[i].Hidden == True:
                    Tiles[i].Flag = False
                elif Tiles[i].Flag == False and Tiles[i].Hidden == True:
                    Tiles[i].Flag = True



font = pygame.font.SysFont("arial",100)

Board = Board(25,15,30,50)

Tile0,Tile1,Tile2,Tile3,Tile4,Tile5,Tile6,Tile7,Tile8,Tile9,Tile10,Tile11,Tile12,Tile13,Tile14,Tile15,Tile16,Tile17,Tile18,Tile19,Tile20,Tile21,Tile22,Tile23,Tile24,Tile25,Tile26,Tile27,Tile28,Tile29,Tile30,Tile31,Tile32,Tile33,Tile34,Tile35,Tile36,Tile37,Tile38,Tile39,Tile40,Tile41,Tile42,Tile43,Tile44,Tile45,Tile46,Tile47,Tile48,Tile49,Tile50,Tile51,Tile52,Tile53,Tile54,Tile55,Tile56,Tile57,Tile58,Tile59,Tile60,Tile61,Tile62,Tile63,Tile64,Tile65,Tile66,Tile67,Tile68,Tile69,Tile70,Tile71,Tile72,Tile73,Tile74,Tile75,Tile76,Tile77,Tile78,Tile79,Tile80,Tile81,Tile82,Tile83,Tile84,Tile85,Tile86,Tile87,Tile88,Tile89,Tile90,Tile91,Tile92,Tile93,Tile94,Tile95,Tile96,Tile97,Tile98,Tile99,Tile100,Tile101,Tile102,Tile103,Tile104,Tile105,Tile106,Tile107,Tile108,Tile109,Tile110,Tile111,Tile112,Tile113,Tile114,Tile115,Tile116,Tile117,Tile118,Tile119,Tile120,Tile121,Tile122,Tile123,Tile124,Tile125,Tile126,Tile127,Tile128,Tile129,Tile130,Tile131,Tile132,Tile133,Tile134,Tile135,Tile136,Tile137,Tile138,Tile139,Tile140,Tile141,Tile142,Tile143,Tile144,Tile145,Tile146,Tile147,Tile148,Tile149,Tile150,Tile151,Tile152,Tile153,Tile154,Tile155,Tile156,Tile157,Tile158,Tile159,Tile160,Tile161,Tile162,Tile163,Tile164,Tile165,Tile166,Tile167,Tile168,Tile169,Tile170,Tile171,Tile172,Tile173,Tile174,Tile175,Tile176,Tile177,Tile178,Tile179,Tile180,Tile181,Tile182,Tile183,Tile184,Tile185,Tile186,Tile187,Tile188,Tile189,Tile190,Tile191,Tile192,Tile193,Tile194,Tile195,Tile196,Tile197,Tile198,Tile199,Tile200,Tile201,Tile202,Tile203,Tile204,Tile205,Tile206,Tile207,Tile208,Tile209,Tile210,Tile211,Tile212,Tile213,Tile214,Tile215,Tile216,Tile217,Tile218,Tile219,Tile220,Tile221,Tile222,Tile223,Tile224,Tile225,Tile226,Tile227,Tile228,Tile229,Tile230,Tile231,Tile232,Tile233,Tile234,Tile235,Tile236,Tile237,Tile238,Tile239,Tile240,Tile241,Tile242,Tile243,Tile244,Tile245,Tile246,Tile247,Tile248,Tile249,Tile250,Tile251,Tile252,Tile253,Tile254,Tile255,Tile256,Tile257,Tile258,Tile259,Tile260,Tile261,Tile262,Tile263,Tile264,Tile265,Tile266,Tile267,Tile268,Tile269,Tile270,Tile271,Tile272,Tile273,Tile274,Tile275,Tile276,Tile277,Tile278,Tile279,Tile280,Tile281,Tile282,Tile283,Tile284,Tile285,Tile286,Tile287,Tile288,Tile289,Tile290,Tile291,Tile292,Tile293,Tile294,Tile295,Tile296,Tile297,Tile298,Tile299,Tile300,Tile301,Tile302,Tile303,Tile304,Tile305,Tile306,Tile307,Tile308,Tile309,Tile310,Tile311,Tile312,Tile313,Tile314,Tile315,Tile316,Tile317,Tile318,Tile319,Tile320,Tile321,Tile322,Tile323,Tile324,Tile325,Tile326,Tile327,Tile328,Tile329,Tile330,Tile331,Tile332,Tile333,Tile334,Tile335,Tile336,Tile337,Tile338,Tile339,Tile340,Tile341,Tile342,Tile343,Tile344,Tile345,Tile346,Tile347,Tile348,Tile349,Tile350,Tile351,Tile352,Tile353,Tile354,Tile355,Tile356,Tile357,Tile358,Tile359,Tile360,Tile361,Tile362,Tile363,Tile364,Tile365,Tile366,Tile367,Tile368,Tile369,Tile370,Tile371,Tile372,Tile373,Tile374,Tile375,Tile376,Tile377,Tile378,Tile379,Tile380,Tile381,Tile382,Tile383,Tile384,Tile385,Tile386,Tile387,Tile388,Tile389,Tile390,Tile391,Tile392,Tile393,Tile394,Tile395,Tile396,Tile397,Tile398,Tile399,Tile400,Tile401,Tile402,Tile403,Tile404,Tile405,Tile406,Tile407,Tile408,Tile409,Tile410,Tile411,Tile412,Tile413,Tile414,Tile415,Tile416,Tile417,Tile418,Tile419,Tile420,Tile421,Tile422,Tile423,Tile424,Tile425,Tile426,Tile427,Tile428,Tile429,Tile430,Tile431,Tile432,Tile433,Tile434,Tile435,Tile436,Tile437,Tile438,Tile439,Tile440,Tile441,Tile442,Tile443,Tile444,Tile445,Tile446,Tile447,Tile448,Tile449,Tile450,Tile451,Tile452,Tile453,Tile454,Tile455,Tile456,Tile457,Tile458,Tile459,Tile460,Tile461,Tile462,Tile463,Tile464,Tile465,Tile466,Tile467,Tile468,Tile469,Tile470,Tile471,Tile472,Tile473,Tile474,Tile475,Tile476,Tile477,Tile478,Tile479,Tile480,Tile481,Tile482,Tile483,Tile484,Tile485,Tile486,Tile487,Tile488,Tile489,Tile490,Tile491,Tile492,Tile493,Tile494,Tile495,Tile496,Tile497,Tile498,Tile499 = Tile(0),Tile(1),Tile(2),Tile(3),Tile(4),Tile(5),Tile(6),Tile(7),Tile(8),Tile(9),Tile(10),Tile(11),Tile(12),Tile(13),Tile(14),Tile(15),Tile(16),Tile(17),Tile(18),Tile(19),Tile(20),Tile(21),Tile(22),Tile(23),Tile(24),Tile(25),Tile(26),Tile(27),Tile(28),Tile(29),Tile(30),Tile(31),Tile(32),Tile(33),Tile(34),Tile(35),Tile(36),Tile(37),Tile(38),Tile(39),Tile(40),Tile(41),Tile(42),Tile(43),Tile(44),Tile(45),Tile(46),Tile(47),Tile(48),Tile(49),Tile(50),Tile(51),Tile(52),Tile(53),Tile(54),Tile(55),Tile(56),Tile(57),Tile(58),Tile(59),Tile(60),Tile(61),Tile(62),Tile(63),Tile(64),Tile(65),Tile(66),Tile(67),Tile(68),Tile(69),Tile(70),Tile(71),Tile(72),Tile(73),Tile(74),Tile(75),Tile(76),Tile(77),Tile(78),Tile(79),Tile(80),Tile(81),Tile(82),Tile(83),Tile(84),Tile(85),Tile(86),Tile(87),Tile(88),Tile(89),Tile(90),Tile(91),Tile(92),Tile(93),Tile(94),Tile(95),Tile(96),Tile(97),Tile(98),Tile(99),Tile(100),Tile(101),Tile(102),Tile(103),Tile(104),Tile(105),Tile(106),Tile(107),Tile(108),Tile(109),Tile(110),Tile(111),Tile(112),Tile(113),Tile(114),Tile(115),Tile(116),Tile(117),Tile(118),Tile(119),Tile(120),Tile(121),Tile(122),Tile(123),Tile(124),Tile(125),Tile(126),Tile(127),Tile(128),Tile(129),Tile(130),Tile(131),Tile(132),Tile(133),Tile(134),Tile(135),Tile(136),Tile(137),Tile(138),Tile(139),Tile(140),Tile(141),Tile(142),Tile(143),Tile(144),Tile(145),Tile(146),Tile(147),Tile(148),Tile(149),Tile(150),Tile(151),Tile(152),Tile(153),Tile(154),Tile(155),Tile(156),Tile(157),Tile(158),Tile(159),Tile(160),Tile(161),Tile(162),Tile(163),Tile(164),Tile(165),Tile(166),Tile(167),Tile(168),Tile(169),Tile(170),Tile(171),Tile(172),Tile(173),Tile(174),Tile(175),Tile(176),Tile(177),Tile(178),Tile(179),Tile(180),Tile(181),Tile(182),Tile(183),Tile(184),Tile(185),Tile(186),Tile(187),Tile(188),Tile(189),Tile(190),Tile(191),Tile(192),Tile(193),Tile(194),Tile(195),Tile(196),Tile(197),Tile(198),Tile(199),Tile(200),Tile(201),Tile(202),Tile(203),Tile(204),Tile(205),Tile(206),Tile(207),Tile(208),Tile(209),Tile(210),Tile(211),Tile(212),Tile(213),Tile(214),Tile(215),Tile(216),Tile(217),Tile(218),Tile(219),Tile(220),Tile(221),Tile(222),Tile(223),Tile(224),Tile(225),Tile(226),Tile(227),Tile(228),Tile(229),Tile(230),Tile(231),Tile(232),Tile(233),Tile(234),Tile(235),Tile(236),Tile(237),Tile(238),Tile(239),Tile(240),Tile(241),Tile(242),Tile(243),Tile(244),Tile(245),Tile(246),Tile(247),Tile(248),Tile(249),Tile(250),Tile(251),Tile(252),Tile(253),Tile(254),Tile(255),Tile(256),Tile(257),Tile(258),Tile(259),Tile(260),Tile(261),Tile(262),Tile(263),Tile(264),Tile(265),Tile(266),Tile(267),Tile(268),Tile(269),Tile(270),Tile(271),Tile(272),Tile(273),Tile(274),Tile(275),Tile(276),Tile(277),Tile(278),Tile(279),Tile(280),Tile(281),Tile(282),Tile(283),Tile(284),Tile(285),Tile(286),Tile(287),Tile(288),Tile(289),Tile(290),Tile(291),Tile(292),Tile(293),Tile(294),Tile(295),Tile(296),Tile(297),Tile(298),Tile(299),Tile(300),Tile(301),Tile(302),Tile(303),Tile(304),Tile(305),Tile(306),Tile(307),Tile(308),Tile(309),Tile(310),Tile(311),Tile(312),Tile(313),Tile(314),Tile(315),Tile(316),Tile(317),Tile(318),Tile(319),Tile(320),Tile(321),Tile(322),Tile(323),Tile(324),Tile(325),Tile(326),Tile(327),Tile(328),Tile(329),Tile(330),Tile(331),Tile(332),Tile(333),Tile(334),Tile(335),Tile(336),Tile(337),Tile(338),Tile(339),Tile(340),Tile(341),Tile(342),Tile(343),Tile(344),Tile(345),Tile(346),Tile(347),Tile(348),Tile(349),Tile(350),Tile(351),Tile(352),Tile(353),Tile(354),Tile(355),Tile(356),Tile(357),Tile(358),Tile(359),Tile(360),Tile(361),Tile(362),Tile(363),Tile(364),Tile(365),Tile(366),Tile(367),Tile(368),Tile(369),Tile(370),Tile(371),Tile(372),Tile(373),Tile(374),Tile(375),Tile(376),Tile(377),Tile(378),Tile(379),Tile(380),Tile(381),Tile(382),Tile(383),Tile(384),Tile(385),Tile(386),Tile(387),Tile(388),Tile(389),Tile(390),Tile(391),Tile(392),Tile(393),Tile(394),Tile(395),Tile(396),Tile(397),Tile(398),Tile(399),Tile(400),Tile(401),Tile(402),Tile(403),Tile(404),Tile(405),Tile(406),Tile(407),Tile(408),Tile(409),Tile(410),Tile(411),Tile(412),Tile(413),Tile(414),Tile(415),Tile(416),Tile(417),Tile(418),Tile(419),Tile(420),Tile(421),Tile(422),Tile(423),Tile(424),Tile(425),Tile(426),Tile(427),Tile(428),Tile(429),Tile(430),Tile(431),Tile(432),Tile(433),Tile(434),Tile(435),Tile(436),Tile(437),Tile(438),Tile(439),Tile(440),Tile(441),Tile(442),Tile(443),Tile(444),Tile(445),Tile(446),Tile(447),Tile(448),Tile(449),Tile(450),Tile(451),Tile(452),Tile(453),Tile(454),Tile(455),Tile(456),Tile(457),Tile(458),Tile(459),Tile(460),Tile(461),Tile(462),Tile(463),Tile(464),Tile(465),Tile(466),Tile(467),Tile(468),Tile(469),Tile(470),Tile(471),Tile(472),Tile(473),Tile(474),Tile(475),Tile(476),Tile(477),Tile(478),Tile(479),Tile(480),Tile(481),Tile(482),Tile(483),Tile(484),Tile(485),Tile(486),Tile(487),Tile(488),Tile(489),Tile(490),Tile(491),Tile(492),Tile(493),Tile(494),Tile(495),Tile(496),Tile(497),Tile(498),Tile(499)

Tiles = [Tile0,Tile1,Tile2,Tile3,Tile4,Tile5,Tile6,Tile7,Tile8,Tile9,Tile10,Tile11,Tile12,Tile13,Tile14,Tile15,Tile16,Tile17,Tile18,Tile19,Tile20,Tile21,Tile22,Tile23,Tile24,Tile25,Tile26,Tile27,Tile28,Tile29,Tile30,Tile31,Tile32,Tile33,Tile34,Tile35,Tile36,Tile37,Tile38,Tile39,Tile40,Tile41,Tile42,Tile43,Tile44,Tile45,Tile46,Tile47,Tile48,Tile49,Tile50,Tile51,Tile52,Tile53,Tile54,Tile55,Tile56,Tile57,Tile58,Tile59,Tile60,Tile61,Tile62,Tile63,Tile64,Tile65,Tile66,Tile67,Tile68,Tile69,Tile70,Tile71,Tile72,Tile73,Tile74,Tile75,Tile76,Tile77,Tile78,Tile79,Tile80,Tile81,Tile82,Tile83,Tile84,Tile85,Tile86,Tile87,Tile88,Tile89,Tile90,Tile91,Tile92,Tile93,Tile94,Tile95,Tile96,Tile97,Tile98,Tile99,Tile100,Tile101,Tile102,Tile103,Tile104,Tile105,Tile106,Tile107,Tile108,Tile109,Tile110,Tile111,Tile112,Tile113,Tile114,Tile115,Tile116,Tile117,Tile118,Tile119,Tile120,Tile121,Tile122,Tile123,Tile124,Tile125,Tile126,Tile127,Tile128,Tile129,Tile130,Tile131,Tile132,Tile133,Tile134,Tile135,Tile136,Tile137,Tile138,Tile139,Tile140,Tile141,Tile142,Tile143,Tile144,Tile145,Tile146,Tile147,Tile148,Tile149,Tile150,Tile151,Tile152,Tile153,Tile154,Tile155,Tile156,Tile157,Tile158,Tile159,Tile160,Tile161,Tile162,Tile163,Tile164,Tile165,Tile166,Tile167,Tile168,Tile169,Tile170,Tile171,Tile172,Tile173,Tile174,Tile175,Tile176,Tile177,Tile178,Tile179,Tile180,Tile181,Tile182,Tile183,Tile184,Tile185,Tile186,Tile187,Tile188,Tile189,Tile190,Tile191,Tile192,Tile193,Tile194,Tile195,Tile196,Tile197,Tile198,Tile199,Tile200,Tile201,Tile202,Tile203,Tile204,Tile205,Tile206,Tile207,Tile208,Tile209,Tile210,Tile211,Tile212,Tile213,Tile214,Tile215,Tile216,Tile217,Tile218,Tile219,Tile220,Tile221,Tile222,Tile223,Tile224,Tile225,Tile226,Tile227,Tile228,Tile229,Tile230,Tile231,Tile232,Tile233,Tile234,Tile235,Tile236,Tile237,Tile238,Tile239,Tile240,Tile241,Tile242,Tile243,Tile244,Tile245,Tile246,Tile247,Tile248,Tile249,Tile250,Tile251,Tile252,Tile253,Tile254,Tile255,Tile256,Tile257,Tile258,Tile259,Tile260,Tile261,Tile262,Tile263,Tile264,Tile265,Tile266,Tile267,Tile268,Tile269,Tile270,Tile271,Tile272,Tile273,Tile274,Tile275,Tile276,Tile277,Tile278,Tile279,Tile280,Tile281,Tile282,Tile283,Tile284,Tile285,Tile286,Tile287,Tile288,Tile289,Tile290,Tile291,Tile292,Tile293,Tile294,Tile295,Tile296,Tile297,Tile298,Tile299,Tile300,Tile301,Tile302,Tile303,Tile304,Tile305,Tile306,Tile307,Tile308,Tile309,Tile310,Tile311,Tile312,Tile313,Tile314,Tile315,Tile316,Tile317,Tile318,Tile319,Tile320,Tile321,Tile322,Tile323,Tile324,Tile325,Tile326,Tile327,Tile328,Tile329,Tile330,Tile331,Tile332,Tile333,Tile334,Tile335,Tile336,Tile337,Tile338,Tile339,Tile340,Tile341,Tile342,Tile343,Tile344,Tile345,Tile346,Tile347,Tile348,Tile349,Tile350,Tile351,Tile352,Tile353,Tile354,Tile355,Tile356,Tile357,Tile358,Tile359,Tile360,Tile361,Tile362,Tile363,Tile364,Tile365,Tile366,Tile367,Tile368,Tile369,Tile370,Tile371,Tile372,Tile373,Tile374,Tile375,Tile376,Tile377,Tile378,Tile379,Tile380,Tile381,Tile382,Tile383,Tile384,Tile385,Tile386,Tile387,Tile388,Tile389,Tile390,Tile391,Tile392,Tile393,Tile394,Tile395,Tile396,Tile397,Tile398,Tile399,Tile400,Tile401,Tile402,Tile403,Tile404,Tile405,Tile406,Tile407,Tile408,Tile409,Tile410,Tile411,Tile412,Tile413,Tile414,Tile415,Tile416,Tile417,Tile418,Tile419,Tile420,Tile421,Tile422,Tile423,Tile424,Tile425,Tile426,Tile427,Tile428,Tile429,Tile430,Tile431,Tile432,Tile433,Tile434,Tile435,Tile436,Tile437,Tile438,Tile439,Tile440,Tile441,Tile442,Tile443,Tile444,Tile445,Tile446,Tile447,Tile448,Tile449,Tile450,Tile451,Tile452,Tile453,Tile454,Tile455,Tile456,Tile457,Tile458,Tile459,Tile460,Tile461,Tile462,Tile463,Tile464,Tile465,Tile466,Tile467,Tile468,Tile469,Tile470,Tile471,Tile472,Tile473,Tile474,Tile475,Tile476,Tile477,Tile478,Tile479,Tile480,Tile481,Tile482,Tile483,Tile484,Tile485,Tile486,Tile487,Tile488,Tile489,Tile490,Tile491,Tile492,Tile493,Tile494,Tile495,Tile496,Tile497,Tile498,Tile499]



#TilesX,TilesY,TileSize,Bombs

Board.ApplyBombs()
Board.ApplyBombCounter()



for i in range(0,Board.TotalTiles):
    Tiles[i].FindCordOnMap()

def DrawAll():
    Screen.fill((105,190,235))
    for i in range(0,Board.TotalTiles):
        Tiles[i].CheckColor()
        Tiles[i].Draw()



LEFT = 1
RIGHT = 3
while True:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            pygame.QUIT()
            exit()
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == LEFT:
                    Click = "left"
                elif event.button == RIGHT:
                    Click = "right"
                MouseClick(pygame.mouse.get_pos(),Click)
            DrawAll()
            pygame.display.update()













##Tiles = []
##var = ""
##equal = ""
##for i in range(1,501):
##    Tiles.append("Tile"+str(i))
##for i in range(0,500):
##    equal = equal + "Tile(),"
##
##
##for i in range(0,500):
##    var = var + (Tiles[i]+",")
##print(var,"=",equal)
