{
  "targets": [
    {
      "target_name": "scws",
      "sources": [
        "./src/nodescws2.cc",
        "./src/scws2.cc"
      ],
      "include_dirs": [
        "<!(node -e \"require('nan')\")"
      ]
    }
  ]
}
