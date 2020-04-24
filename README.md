# ARACNE

Unofficial Python notebook for the paper [**ARACNE: an Algorithm for the Reconstruction of Gene Regulatory Networks in a Mammalian Cellular Context**](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-7-S1-S7) by Margolin et al. There is also an implementation to simulate a synthetic network and its dynamics following the paper [**Artificial gene networks for objective comparison of analysis algorithms**](https://academic.oup.com/bioinformatics/article/19/suppl_2/ii122/180406) by Mendes et al.

The problem at hand can be roughly described as: given time series data observation from different nodes, try to infer which ones and how much such nodes are linked. Mutual Information is the measure used to estimate the statistical dependence between nodes.

### Prerequisites

```
Python >= 3
NumPy
Matplotlib
SciPy
```


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


