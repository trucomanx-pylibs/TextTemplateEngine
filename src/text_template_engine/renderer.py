import os
import shutil

def render_string(template_str, variables):
    """
    Render a template string by replacing placeholders with values.

    This function replaces all placeholders in the format
    {{PLACEHOLDER_NAME}} with their corresponding values from
    the provided variables dictionary and returns the rendered
    string.
    
    Parameters
    ----------
    template_str : str
        Template content containing placeholders.
    
    variables : dict[str, str]
        Dictionary mapping placeholder names to replacement values.
        
        Example::
        
            {
                "NAME": "John Doe",
                "EMAIL": "john@example.com"
            }
        
        Template::
        
            Hello {{NAME}}
            Contact: {{EMAIL}}
        
        Result::
        
            Hello John Doe
            Contact: john@example.com
    
    
    Notes
    -----
    - Placeholders are case-sensitive.
    - Placeholders without a matching key remain unchanged.
    - All values are converted to strings before replacement.
    - All replacements are performed as plain text.

    Returns
    -------
    str
        The rendered string with all matching placeholders replaced.

    Example
    -------
    >>> render_string(
    ...     "Hello {{NAME}}",
    ...     {"NAME": "John"}
    ... )
    'Hello John'
    """
    
    content = template_str

    for key, value in variables.items():
        placeholder = "{{" + key + "}}"
        content = content.replace(placeholder, str(value))

    return content
    


def render_file(template_path, output_path, variables):
    """
    Render a text template and save the result to a file.

    This function reads a template file, replaces all placeholders
    in the format {{PLACEHOLDER_NAME}} with the corresponding values
    provided in the variables dictionary, and writes the rendered
    content to the output file.

    If the output directory does not exist, it is created automatically.
    
    Parameters
    ----------
    template_path : str
        Path to the template file containing placeholders.

    output_path : str
        Path where the rendered file will be written.

    variables : dict[str, str]
        Dictionary mapping placeholder names to replacement values.

        Example::
        
            {
                "NAME": "John Doe",
                "EMAIL": "john@example.com"
            }

        Template::
        
            Hello {{NAME}}
            Contact: {{EMAIL}}

        Result::
        
            Hello John Doe
            Contact: john@example.com

    Notes
    -----
    - Placeholders are case-sensitive.
    - Placeholders without a matching key remain unchanged.
    - All replacements are performed as plain text.

    Returns
    -------
    None
    """

    # Lê template
    with open(template_path, "r", encoding="utf-8") as f:
        conteudo = f.read()

    # Substitui placeholders
    conteudo = render_string(conteudo, variables)

    output_dir = os.path.dirname(output_path)

    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    # Salva arquivo final
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(conteudo)

    print(f"Arquivo gerado: {output_path}")
    




def render_directory(template_dir, output_dir, variables, filter=None):
    """
    Render all template files in a directory tree.

    Files whose extensions match the provided filter are rendered
    using the supplied variables. All other files are copied
    unchanged to the output directory.

    Parameters
    ----------
    template_dir : str
        Source directory containing template files.

    output_dir : str
        Destination directory for generated files.

    variables : dict[str, str]
        Placeholder-value mapping used during rendering.

    filter : list[str] | None, optional
        List of file extensions to render.

        Example:
            [".html", ".txt", ".md"]

        If None, all files are rendered.

    Returns
    -------
    None
    """

    for root, _, files in os.walk(template_dir):

        for filename in files:

            source_path = os.path.join(root, filename)

            relative_path = os.path.relpath(
                source_path,
                template_dir
            )

            target_path = os.path.join(
                output_dir,
                relative_path
            )

            should_render = (
                filter is None
                or any(
                    filename.endswith(ext)
                    for ext in filter
                )
            )

            if should_render:
                render_file(
                    source_path,
                    target_path,
                    variables
                )
            else:
                target_dir = os.path.dirname(target_path)

                if target_dir:
                    os.makedirs(
                        target_dir,
                        exist_ok=True
                    )

                shutil.copy2(
                    source_path,
                    target_path
                )
