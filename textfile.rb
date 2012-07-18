# Textfile sublet file
# Created with sur-0.2
configure :textfile do |s|
  s.file = s.config[:file]
  s.watch(s.file)
end

on :watch do |s|
  begin
    self.data = IO.readlines(@file).first.chop
  rescue => err
    print err
    self.data = "ERR"
  end
end
