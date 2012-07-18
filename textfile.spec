# -*- encoding: utf-8 -*-
# Textfile specification file
# Created with sur-0.2
Sur::Specification.new do |s|
  # Sublet information
  s.name        = "Textfile"
  s.version     = "0.1"
  s.tags        = [ "text", "file" ]
  s.files       = [ "textfile.rb" ]
  s.icons       = [ ]

  # Sublet description
  s.description = "Displays the first line of a text file."
  s.notes       = <<NOTES
Taken almost verbatim from an example written by Christoph Kappel:
http://subforge.org/projects/subtle/wiki/Writing_sublets?version=12#Examples
NOTES

  # Sublet authors
  s.authors     = [ "Francois Lebel" ]
  s.contact     = "https://github.com/flebel/sublet-textfile"
  s.date        = "Tue Jul 17 22:24 EDT 2012"

  # Sublet config
  s.config = [
    {
      :name        => "file",
      :type        => "string",
      :description => "Path to the text file",
      :def_value   => ""
    }
  ]
end
