Dataset **Urban Street: Fruit Classification** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogImZzOi8vYXNzZXRzLzI3NTlfVXJiYW4gU3RyZWV0OiBGcnVpdCBDbGFzc2lmaWNhdGlvbi91cmJhbi1zdHJlZXQ6LWZydWl0LWNsYXNzaWZpY2F0aW9uLURhdGFzZXROaW5qYS50YXIiLCAic2lnIjogIm55YXdJOE9iUkdZMEhvMXIxcEowN1pPcHJsLzNENG1pUmc1NUdLOER3azg9In0=)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Urban Street: Fruit Classification', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://www.kaggle.com/datasets/erickendric/tree-dataset-of-urban-street-classification-fruit).