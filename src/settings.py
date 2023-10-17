from typing import Dict, List, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "Urban Street: Fruit Classification"
PROJECT_NAME_FULL: str = "Tree Dataset of Urban Street: Fruit Classification"
HIDE_DATASET = True  # set False when 100% sure about repo quality

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.GNU_GPL_v3()
APPLICATIONS: List[Union[Industry, Domain, Research]] = [Industry.Environmental()]
CATEGORY: Category = Category.Environmental()

CV_TASKS: List[CVTask] = [CVTask.Classification()]
ANNOTATION_TYPES: List[AnnotationType] = []

RELEASE_DATE: Optional[str] = "2022-09-24"  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = None

HOMEPAGE_URL: str = "https://www.kaggle.com/datasets/erickendric/tree-dataset-of-urban-street-classification-fruit"
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 7022746
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/urban-street-fruit"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[Union[str, dict]] = [
    "https://www.kaggle.com/datasets/erickendric/tree-dataset-of-urban-street-classification-fruit"
]
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = None
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

# If you have more than the one paper, put the most relatable link as the first element of the list
# Use dict key to specify name for a button
PAPER: Optional[Union[str, List[str], Dict[str, str]]] = [
    "https://www.sciencedirect.com/science/article/abs/pii/S0168169923002405?via%3Dihub"
]
BLOGPOST: Optional[Union[str, List[str], Dict[str, str]]] = ["https://ytt917251944.github.io/dataset_jekyll/"]
REPOSITORY: Optional[Union[str, List[str], Dict[str, str]]] = {
    "GitHub": "https://github.com/ytt917251944/dataset_jekyll"
}

CITATION_URL: Optional[
    str
] = "https://www.sciencedirect.com/science/article/abs/pii/S0168169923002405?via%3Dihub"
AUTHORS: Optional[List[str]] = [
    "Tingting Yang",
    "Suyin Zhou",
    "Zhijie Huang",
    "Aijun Xu",
    "Junhua Ye",
    "Jianxin Yin",
]

ORGANIZATION_NAME: Optional[Union[str, List[str]]] = [
    "Zhejiang Agriculture and Forestry University"
]
ORGANIZATION_URL: Optional[Union[str, List[str]]] = ["https://www.zafu.edu.cn/"]

# Set '__PRETEXT__' or '__POSTTEXT__' as a key with string value to add custom text. e.g. SLYTAGSPLIT = {'__POSTTEXT__':'some text}
SLYTAGSPLIT: Optional[Dict[str, Union[List[str], str]]] = {
    "classification set classes": [
        "acer_palmatum",
        "albizia_julibrissin",
        "celtis_sinensis",
        "cinnamomum_camphora_(linn)_presl",
        "elaeocarpus_decipiens",
        "euonymus_japonicus",
        "ginkgo_biloba",
        "koelreuteria_paniculata",
        "lagerstroemia_indica",
        "liquidambar_formosana",
        "liriodendron_chinense",
        "llex_cornuta",
        "magnolia_grandiflora_l",
        "magnolia_liliflora_desr",
        "malushalliana",
        "metasequoia_glyptostroboides",
        "michelia_chapensis",
        "nandina_domestica",
        "photinia_serratifolia",
        "pittosporum_tobira",
        "platanus",
        "platycladus_orientalis_beverlevensis",
        "podocarpus_macrophyllus",
        "prunus_cerasifera_f._atropurpurea",
        "prunus_persica",
        "sapindus_saponaria",
        "styphnolobium_japonicum",
        "taxodium_ascendens_brongn",
        "triadica_sebifera",
    ],
}
TAGS: Optional[List[str]] = None


SECTION_EXPLORE_CUSTOM_DATASETS: Optional[List[str]] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError(
            "Please fill all fields in settings.py before uploading to instance."
        )


def get_settings():
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "project_name_full": PROJECT_NAME_FULL or PROJECT_NAME,
        "hide_dataset": HIDE_DATASET,
        "license": LICENSE,
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError(
            "Please fill all fields in settings.py after uploading to instance."
        )

    settings["release_date"] = RELEASE_DATE
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["blog"] = BLOGPOST
    settings["repository"] = REPOSITORY
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    settings["explore_datasets"] = SECTION_EXPLORE_CUSTOM_DATASETS

    return settings
