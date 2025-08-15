Dataset **Urban Street: Fruit Classification** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogInMzOi8vc3VwZXJ2aXNlbHktZGF0YXNldHMvMjc1OV9VcmJhbiBTdHJlZXQ6IEZydWl0IENsYXNzaWZpY2F0aW9uL3VyYmFuLXN0cmVldDotZnJ1aXQtY2xhc3NpZmljYXRpb24tRGF0YXNldE5pbmphLnRhciIsICJzaWciOiAibzNwSm42TkY5cDU3NXlFQ0E1NjhFdWRGenBTL0dRM0VvM3JiWnRiQmI3ND0ifQ==?response-content-disposition=attachment%3B%20filename%3D%22urban-street%3A-fruit-classification-DatasetNinja.tar%22)

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