from docker_distrib_talk import DockerDistributionRequester

r = DockerDistributionRequester("registry.centos.org")
for item in r.get_all_repos():
    print "Image : " + item + "\n"
    for item1 in r.get_repo_tags(item):
        print " * TAG : " + item1 + "\n"
        print r.get_image_manifest(item, item1)
        print "\n"
    print "\n"
