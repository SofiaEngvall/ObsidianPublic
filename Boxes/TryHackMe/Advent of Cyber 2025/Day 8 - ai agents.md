
`reset_holiday`: Requires `token`, `desired_theme`, and `dry_run`.
desired_theme = enum of ['SOCMAS', 'EASTMAS']

`booking_a_calendar`: Needs `title`, `date`, `start/end`, `theme`, `note`, `created_by`, and `token`.

`get_logs`: Accepts `query`, `level`, `subsystem`, and `limit`.

**Dry run request**: Provide `dry_run` to simulate the actual use without affecting global settings.

**Actual run request**: Use the provided functions with required parameters and optional tokens.

reset_holiday('SOCMAS')