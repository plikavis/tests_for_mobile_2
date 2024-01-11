def abs_path_from_project(relative_path: str):
    import tests_for_mobile_2
    from pathlib import Path
    return (
        Path(tests_for_mobile_2.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )