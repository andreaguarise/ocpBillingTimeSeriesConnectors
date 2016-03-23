import Config


conf = Config.Config('./test.conf')
conf.read()
print conf.get("Pillar","baseUri")
print conf.items("Metrics")