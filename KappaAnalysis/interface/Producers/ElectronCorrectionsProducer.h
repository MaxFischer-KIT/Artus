
#pragma once

#include "Kappa/DataFormats/interface/Kappa.h"

#include "Artus/KappaAnalysis/interface/KappaProducerBase.h"


/**
   \brief Producer for electron four momentum corrections.
   
   (No correction implemented yet.)
*/
class ElectronCorrectionsProducer: public KappaProducerBase
{

public:

	virtual std::string GetProducerId() const override;
	
	virtual void Init(KappaSettings const& settings)  override;

	virtual void Produce(KappaEvent const& event, KappaProduct & product,
	                     KappaSettings const& settings) const override;


protected:

	// Can be overwritten for analysis-specific use cases
	virtual void AdditionalCorrections(KElectron* electron, KappaEvent const& event,
	                                   KappaProduct& product, KappaSettings const& settings) const
	{
	}

};

