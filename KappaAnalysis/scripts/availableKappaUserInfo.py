#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import Artus.Utility.logger as logger
log = logging.getLogger(__name__)

import argparse
import os

import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
ROOT.gErrorIgnoreLevel = ROOT.kError


def main():
	ROOT.gROOT.SetBatch(True)
	ROOT.gSystem.Load(os.path.expandvars("$CMSSW_BASE/src/Kappa/lib/libKappa"))
	
	parser = argparse.ArgumentParser(description="Print out the user info in the kappa skim.", parents=[logger.loggingParser])
	parser.add_argument("file", help="Kappa skim output file containing the UserInfo in the Lumis tree")
	parser.add_argument("-k", "--keys", nargs="+",
	                    help="Keys to print. [Default: print available keys]")
	args = parser.parse_args()
	logger.initLogger(args)
	
	root_file = ROOT.TFile(args.file, "READ")
	lumis = root_file.Get("Lumis")
	lumis.GetEntry(0)
	
	user_infos = lumis.GetUserInfo()
	assert user_infos.GetEntries() >= 2
	keys = user_infos[0]
	values = user_infos[1]
	
	user_infos_dict = { str(k.GetString()) : str(v.GetString()) for k, v in zip(keys, values) }
	
	if args.keys is None:
		log.info("Available keys:")
		for key in user_infos_dict.keys():
			log.info("\t%s" % key)
	else:
		if len(args.keys) == 1:
			if args.keys[0] in user_infos_dict:
				log.info(user_infos_dict[args.keys[0]])
			else:
				log.error("Key \"%s\" not available!" % args.keys[0])
		else:
			for key in args.keys:
				if key in user_infos_dict:
					log.info("%25s : %s" % (key, user_infos_dict[key]))
				else:
					log.error("Key \"%s\" not available!" % key)


if __name__ == "__main__":
	main()

