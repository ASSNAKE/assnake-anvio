import click, glob, os
import assnake.api.loaders
import assnake
from assnake.cli.cli_utils import sample_set_construction_options, add_options, generic_command_individual_samples,\
    generate_result_list, generic_command_dict_of_sample_sets, prepare_sample_set_tsv_and_get_results
from assnake.core.result import Result

@click.command('anvio-gen-db', short_help='Calculate completeness and contamination metrics for your MAGs')
@add_options(sample_set_construction_options)

@click.option('--min-len','-l', help='Minimum length of contigs', default=1000)
@click.option('--overwrite', is_flag=True, help='Overwrite existing sample_set.tsv files', default=False)

@click.pass_obj

def anvio_gen_db_invocation(config, min_len,overwrite, **kwargs):
    # load sample sets     
    sample_sets = generic_command_dict_of_sample_sets(config,   **kwargs)

    sample_set_dir_wc = '{fs_prefix}/{df}/assembly/{sample_set}/'
    result_wc = '{fs_prefix}/{df}/assembly/{sample_set}/megahit__v1.2.9__def/final_contigs__{mod}.db'
    res_list = prepare_sample_set_tsv_and_get_results(sample_set_dir_wc, result_wc, df = kwargs['df'], sample_sets = sample_sets, mod = min_len, overwrite = overwrite)

    config['requests'] += res_list


this_dir = os.path.dirname(os.path.abspath(__file__))
result = Result.from_location(name = 'anvio-gen-db', location = this_dir, input_type = 'illumina_sample_set', additional_inputs = None, invocation_command = anvio_gen_db_invocation)
