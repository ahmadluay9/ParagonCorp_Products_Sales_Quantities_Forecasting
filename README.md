# paragoncorp_products_sales_quantities_forecasting

The objective of this topic is to develop a reliable and accurate forecasting model for predicting products sales quantities, which involves utilizing historical sales data to identify patterns and trends that can inform future sales predictions. By achieving this objective, businesses can effectively plan and adjust their inventory, staffing, and production levels to meet consumer demand while minimizing wastage and maximizing profits.

Model Deployment [Link](https://huggingface.co/spaces/ahmadluay/paragoncorp_products_sales_quantities_forecasting)

# File Explanation on Github

This repository consists of several files, namely :

- Folder `deployment` = Contains files used for *deployment* to `HuggingFace` (contains models, python applications etc.)
- `notebook_paragorncorp_Ahmad_Luay_Adnani.ipynb` = This file is the main *notebook* used to explore dataset and built model
- `inference_paragorncorp_Ahmad_Luay_Adnani.ipynb`= *Notebook* used for *testing inference*. Inferencing is done on a separate *notebook* to prove that the model can run on a *notebook* that is *clean* of variables
- `url.txt` = Deployment URL to HuggingFace

# Conclusion

- SARIMA model: The value of MAPE for this model is 11.6%, and the value of MAE is 594,197. Despite this, the error is considered small because the range of product sales quantities is from 128,808 to 7,172,144.
- Linear Regression model: The value of MAPE for this model is 12.44%, and the value of MAE is 540,970. Despite this, the error is considered small because the range of product sales quantities is from 1,334,134 to 7,172,144.
- The selected model is the model that has the smallest MAPE value which is SARIMA.
