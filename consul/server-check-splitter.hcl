

kind = "service-splitter"
name = "server-check"
splits = [
  {
    weight         = 50
    service				 = "server-b"
  },
  {
    weight         = 50
    service				 = "server-b-test"
  },
]