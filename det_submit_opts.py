def det_submit_opts(job):
    """
    determine submit options from added easyconfigs
    Args:
        job (Job): namedtuple containing all information about job to be submitted

    Returns:
        (string): string containing extra submit options
    """
    submit_opts = [job.slurm_opts]
    submit_opts.append('--comment="some extra options"')

    return ' '.join(submit_opts)
