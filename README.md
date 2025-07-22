### Towards holistic forest monitoring in Europe: An exploration of forest definitions, cultural ecosystem services and their interactions in Germany’s Natura 2000 sites

#### Summary

This repository contains all the scripts for my MSc thesis at the University of Zurich. The files are generally organised by my three research questions (RQs):

1)	**What is considered to be forest?** How do different forest definitions and their geospatial operationalisations change what is counted as forest in the Natura 2000 network in Germany? Where is there consensus on forest presence and where is there no consensus?
2)	**How do people value forests?** What cultural ecosystem services are experienced by people recreating in forests in the Natura 2000 network in Germany?
3)	**How does the way people value forest relate to forest definition?** Do the observed cultural ecosystem services change in areas where there is consensus on forest presence compared to areas where there is no consensus?

To answer these research questions I use a combination of geospatial analysis (RQ1) and natural language processing (RQ2/RQ3). 

#### Using the code

I performed the analysis for all three research questions in a Python (3.12.7) conda environment ([environment.yml](environment.yml)). The steps for each research question alongside commented code in Juypter Notebooks. To create some of the final figures I also made use of R (Rmd available in this repository) and manual map creation in QGIS. 

For **RQ1** the relevant files (in order of use) are: 
1. [rq1_step1_data_prep.ipynb](rq1_step1_data_prep.ipynb) (which runs rq1_step1_sub1_rasterise.bat, rq1_step1_sub2_upsample.bat and rq1_step1_sub3_clip.bat)
2. rq1_step2_fao_forest.ipynb
3. rq1_step3_comp.ipynb
4. rq1_step4_visualisations.rmd

For **RQ2** the relevant files (in order of use) are: 
1. rq2_step1_data_collection.ipynb (with relevant information in scrapy_setup_info.md and scraping tools in the wikiloc_scrapy folder)
2. rq2_step2_text_analysis.ipynb

For **RQ3** the processing script is contained in rq3_all_steps.ipynb, however this script relies on the outputs from RQ1 and RQ2. 


#### Output preview

*For RQ1: Forest consensus map (a) with examples of Natura 2000 sites with no consensus on forest presence (b) and full consensus on forest presence (c). Note the map itself is output by code in this repository, but I created this particular figure in QGIS*

<img src="other/figure_selection/rq1_consenus_summary_3_map.png" alt="forest consensus" width="525" height="375" />

*For RQ2: Word clouds generated from Wikiloc trail text for forest areas in Natura 2000 sites. After cleaning and filtering, text was vectorised using a word2vec model and then clustered using K-means.*

<img src="other/figure_selection/rq2_word_clouds.png" alt="word clouds" width="600" height="480" />

*For RQ3: A comparison of the word/token frequencies for clusters of interest in areas where there is no consensus on forest presence versus areas where there is full consensus.*

<img src="other/figure_selection/rq3_token_counts_per_cluster_class.png" alt="word frequency comparison" width="560" height="630" />


#### Data & Method Information

To answer my research questions, I made use of open-access datasets and methods published in scientific journals. Due to size limitations, this repository does not contain the original data used in the processing steps, however references and access information are provided in the relevant Jupyter Notebooks. For clarity, this information is also summarised below:

For **RQ1**, I relied on the following datasets:

- Hansen Global Forest Change (Hansen et al, 2013)
- ESA CCI Land Cover (Copernicus Climate Change Service, Climate Data Store, 2019)
- JAXA ALOS-2 PALSAR-2 Forest/Non-Forest (Shimada et al, 2014)
- CORINE Land Cover (Copernicus Land Monitoring Service, 2020)
- LBM-DE / CORINE Land Cover 5 ha (Bundesamt für Kartographie und Geodäsie, 2021)
- Natura 2000 Protected Sites (European Environment Agency, 2024)

Further details and download information for these datasets are provided in rq1_step1_data_prep.ipynb under Step 1. As part of RQ1, I also replicated the general methodologies from Sexton et al (2016) for creating the forest consensus map and Johnson et al (2023) for creating an FAO-aligned forest map.

For the data collection for **RQ2**, I built upon the public repository [Wiki4CES](https://github.com/achaiallah-hub/Wiki4CES) by Dr. Chai-allah from the publication Chai-allah et al (2023). This repository scrapes URLs and trail content from the outdoor trail platform [Wikiloc](https://www.wikiloc.com). My modifcations to the scraping tools from Wiki4CES are described in rq2_step1_data_collection.ipynb and scrapy_setup_info.md and are indicated with comments in the scraping spiders provided in the wikiloc_scrapy folder. Additionally, for RQ2 I replicated some of the general methods from Chai-allah et al (2023).

As **RQ3** uses a combination of the outputs from RQ1 and RQ2, no additional data was required.

#### Acknowledgements

A sincere thank you to Prof. Dr. Ross Purves for his supervision on this project. Thank you also to Dr. Abdesslam Chai-allah for providing his [Wiki4CES](https://github.com/achaiallah-hub/Wiki4CES) repository, as well as additional information and encouragement. 

#### Contact Information

For questions about this repository or my thesis, please contact me at <a href="ninadanielle.moffat\@uzh.ch">ninadanielle.moffat\@uzh.ch</a> 

#### Citations

Bundesamt für Kartographie und Geodäsie. (2021). *CORINE Land Cover 5 ha, Stand 2018 (CLC5-2018)*. https://sgx.geodatenzentrum.de/web_public/gdz/dokumentation/deu/clc5_2018.pdf

Copernicus Climate Change Service, Climate Data Store. (2019). Land cover classification gridded maps from 1992 to present derived from satellite observation. *Copernicus Climate Change Service (C3S) Climate Data Store (CDS).* https://doi.org/10.24381/cds.006f2c9a

Copernicus Land Monitoring Service. (2020). *CORINE Land Cover 2018 (vector/raster 100 m), Europe, 6-yearly.* https://doi.org/10.2909/960998c1-1870-4e82-8051-6485205ebbac

Chai-allah, A., Fox, N., Günther, F., Bentayeb, F., Brunschwig, G., Bimonte, S., & Joly, F. (2023). Mining crowdsourced text to capture hikers’ perceptions associated with landscape features and outdoor physical activities. *Ecological Informatics, 78,* 102332. https://doi.org/10.1016/j.ecoinf.2023.102332

European Environment Agency. (2024). Natura 2000 (vector)—Version 2022. *EEA Datahub.* https://www.eea.europa.eu/en/datahub/datahubitem-view/6fc8ad2d-195d-40f4-bdec-576e7d1268e4?activeAccordion=1091667

Hansen, M. C., Potapov, P. V., Moore, R., Hancher, M., Turubanova, S. A., Tyukavina, A., Thau, D., Stehman, S. V., Goetz, S. J., Loveland, T. R., Kommareddy, A., Egorov, A., Chini, L., Justice, C. O., & Townshend, J. R. G. (2013). High-Resolution Global Maps of 21st-Century Forest Cover Change. *Science, 342*(6160), 850–853. https://doi.org/10.1126/science.1244693

Johnson, B. A., Umemiya, C., Magcale-Macandog, D. B., Estoque, R. C., Hayashi, M., & Tadono, T. (2023). Better monitoring of forests according to FAO’s definitions through map integration: Significance and limitations in the context of global environmental goals. *International Journal of Applied Earth Observation and Geoinformation, 122,* 103452. https://doi.org/10.1016/j.jag.2023.103452

Sexton, J. O., Noojipady, P., Song, X.-P., Feng, M., Song, D.-X., Kim, D.-H., Anand, A., Huang, C., Channan, S., Pimm, S. L., & Townshend, J. R. (2016). Conservation policy and the measurement of forests. *Nature Climate Change, 6*(2), 192–196. https://doi.org/10.1038/nclimate2816

Shimada, M., Itoh, T., Motooka, T., Watanabe, M., Shiraishi, T., Thapa, R., & Lucas, R. (2014). New global forest/non-forest maps from ALOS PALSAR data (2007–2010). *Remote Sensing of Environment, 155,* 13–31. https://doi.org/10.1016/j.rse.2014.04.014