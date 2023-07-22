from kedro.pipeline import Pipeline, node, pipeline

from .nodes import preprocess_ames


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=preprocess_ames,
                inputs="ames",
                outputs="preprocessed_ames",
                name="preprocess_ames_node",
            ),
        ]
    )
