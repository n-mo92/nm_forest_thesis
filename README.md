### Towards holistic forest monitoring in Europe: An exploration of forest definitions, cultural ecosystem services and their interactions in Germany’s Natura 2000 sites

This repository contains all the scripts for my MSc thesis at the University of Zurich. The files are generally organised by my three research questions (RQs):

1)	**What is considered to be forest?** How do different forest definitions and their geospatial operationalisations change what is counted as forest in the Natura 2000 network in Germany? Where is there consensus on forest presence and where is there no consensus?
2)	**How do people value forests?** What cultural ecosystem services are experienced by people recreating in forests in the Natura 2000 network in Germany?
3)	**How does the way people value forest relate to forest definition?** Do the observed cultural ecosystem services change in areas where there is consensus on forest presence compared to areas where there is no consensus?

To answer these research questions I use a combination of geospatial analysis (RQ1) and natural language processing (RQ2/RQ3). I have documented the steps for each RQ alongside the code in the Juypter Notebook and R Markdown files. 

**A preview of some of the outputs:**

*For RQ1: Forest consensus map (a) with examples of Natura 2000 sites with no consensus on forest presence (b) and full consensus on forest presence (c).*

<img src="other/figure_selection/rq1_consenus_summary_3_map.png" alt="forest consensus" width="525" height="375" />

*For RQ2: Word clouds generated from Wikiloc trail text for forest areas in Natura 2000 sites. after cleaning and filtering, text was vectorised using a word2vec model and then clustered using K-means.*

<img src="other/figure_selection/rq2_word_clouds.png" alt="word clouds" width="600" height="480" />

*For RQ3: A comparison of the word/token frequencies for clusters of interest in areas where there is no consensus on forest presence versus areas where there is full consensus.*

<img src="other/figure_selection/rq3_token_counts_per_cluster_class.png" alt="word frequency comparison" width="560" height="630" />





