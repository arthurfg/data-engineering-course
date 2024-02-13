import pandas as pd
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def rename_columns(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here
    columns = {
        "VendorID": "vendor_id",
        "RatecodeID": "ratecode_id",
        "PULocationID": "pu_location_id",
        "DOLocationID": "do_location_id",




    }
    data.rename(columns= columns, inplace = True)
    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
@test
def test_passenger_count(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output['passenger_count'].isin([0]).sum() == 0, 'There are rides with 0 passengers'

@test
def test_trip_distance(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output['trip_distance'].isin([0]).sum() == 0, 'There are rides with trip distance of zero'

