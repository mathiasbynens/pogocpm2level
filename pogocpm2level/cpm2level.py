#!/usr/bin/env python
# coding=utf-8

# https://www.reddit.com/r/TheSilphRoad/comments/50w3lx/precise_cp_multiplier_values_for_each_level_help/
LEVEL_TO_CPM = {
	1.0: 0.09399999678134918,
	1.5: 0.13513743132352830,
	2.0: 0.16639786958694458,
	2.5: 0.19265091419219970,
	3.0: 0.21573247015476227,
	3.5: 0.23657265305519104,
	4.0: 0.25572004914283750,
	4.5: 0.27353037893772125,
	5.0: 0.29024988412857056,
	5.5: 0.30605737864971160,
	6.0: 0.32108759880065920,
	6.5: 0.33544503152370453,
	7.0: 0.34921267628669740,
	7.5: 0.36245773732662200,
	8.0: 0.37523558735847473,
	8.5: 0.38759241108516856,
	9.0: 0.39956727623939514,
	9.5: 0.41119354951725060,
	10.0: 0.4225000143051148,
	10.5: 0.4329264134104144,
	11.0: 0.4431075453758240,
	11.5: 0.4530599538719858,
	12.0: 0.4627983868122100,
	12.5: 0.4723360780626535,
	13.0: 0.4816849529743195,
	13.5: 0.4908558102324605,
	14.0: 0.4998584389686584,
	14.5: 0.5087017565965652,
	15.0: 0.5173939466476440,
	15.5: 0.5259425118565559,
	16.0: 0.5343543291091919,
	16.5: 0.5426357612013817,
	17.0: 0.5507926940917969,
	17.5: 0.5588305993005633,
	18.0: 0.5667545199394226,
	18.5: 0.5745691470801830,
	19.0: 0.5822789072990417,
	19.5: 0.5898879119195044,
	20.0: 0.5974000096321106,
	20.5: 0.6048236563801765,
	21.0: 0.6121572852134705,
	21.5: 0.6194041110575199,
	22.0: 0.6265671253204346,
	22.5: 0.6336491815745830,
	23.0: 0.6406529545783997,
	23.5: 0.6475809663534164,
	24.0: 0.6544356346130370,
	24.5: 0.6612192690372467,
	25.0: 0.6679340004920960,
	25.5: 0.6745819002389908,
	26.0: 0.6811649203300476,
	26.5: 0.6876849085092545,
	27.0: 0.6941436529159546,
	27.5: 0.7005428969860077,
	28.0: 0.7068842053413391,
	28.5: 0.7131690979003906,
	29.0: 0.7193990945816040,
	29.5: 0.7255756109952927,
	30.0: 0.7317000031471252,
	30.5: 0.7347410172224045,
	31.0: 0.7377694845199585,
	31.5: 0.7407855764031410,
	32.0: 0.7437894344329834,
	32.5: 0.7467812150716782,
	33.0: 0.7497610449790955,
	33.5: 0.7527291029691696,
	34.0: 0.7556855082511902,
	34.5: 0.7586303651332855,
	35.0: 0.7615638375282288,
	35.5: 0.7644860669970512,
	36.0: 0.76739717, # TODO
	36.5: 0.77029727, # TODO
	37.0: 0.7731865, # TODO
	37.5: 0.77606494, # TODO
	38.0: 0.77893275, # TODO
	38.5: 0.78179006, # TODO
	39.0: 0.78463697, # TODO
	39.5: 0.78747358, # TODO
	40.0: 0.79030001, # TODO
	40.5: 1, # TODO
}

def cpm2level(cpm):
	smallest_diff = 1
	level = 0.0
	for k, v in LEVEL_TO_CPM.items():
		diff = abs(cpm - v)
		if diff < smallest_diff:
			smallest_diff = diff
			level = k
	#print 'Found', smallest_diff, level
	return level
