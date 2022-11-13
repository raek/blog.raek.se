SITE ?= localhost

posts := $(shell bin/find_posts)
static_files := $(shell find src/static/ -type f -printf "%P\n")
upload_destination := $(shell bin/json_query src/sites/$(SITE).json .uploadDestination)

.PHONY: preview
preview: generate
	bin/json_query src/sites/$(SITE).json .urlBase
	cd out/$(SITE); python3 -m http.server

.PHONY: upload
upload: generate
	rsync --verbose --archive --delete out/$(SITE)/ $(upload_destination)/

.PHONY: generate
generate: $(posts:%=out/$(SITE)/%/index.html) \
          $(static_files:%=out/$(SITE)/%) \
          out/$(SITE)/index.html \
          out/$(SITE)/atom-feed.xml
	bin/copy_attachments.py

out/$(SITE)/%/index.html: int/posts/%/merged_post.json \
                  src/templates/post.html
	mkdir -p $(dir $@)
	chevron \
            src/templates/post.html \
	    -d int/posts/$*/merged_post.json \
	    > out/$(SITE)/$*/index.html

int/posts/%/merged_post.json: int/posts/%/body.html \
                       src/blog.json \
                       src/posts/%/post.json
	mkdir -p $(dir $@)
	bin/merge_data.py \
	    site:json:src/sites/$(SITE).json \
	    blog:json:src/blog.json \
	    post:json:src/posts/$*/post.json \
	    body:str:int/posts/$*/body.html \
	    > int/posts/$*/merged_post.json

int/posts/%/body.html: src/posts/%/body.html
	mkdir -p $(dir $@)
	cp $< $@

int/posts/%/body.html: int/posts/%/body.md
	mkdir -p $(dir $@)
	markdown < $< > $@

int/posts/%/body.md: src/posts/%/body.md
	mkdir -p $(dir $@)
	cp $< $@

int/posts/%/body.md: src/posts/%/body.foot.md
	mkdir -p $(dir $@)
	bin/footnotes.py < $< > $@

int/index.json: FORCE
	mkdir -p $(dir $@)
	bin/find_posts | bin/index_posts.py > int/index.json

int/merged_index.json: int/index.json
	mkdir -p $(dir $@)
	bin/merge_data.py \
	    site:json:src/sites/$(SITE).json \
	    blog:json:src/blog.json \
	    index:json:int/index.json \
	    > int/merged_index.json

out/$(SITE)/index.html: int/merged_index.json \
                src/templates/index.html
	mkdir -p $(dir $@)
	chevron \
            src/templates/index.html \
	    -d int/merged_index.json \
	    > out/$(SITE)/index.html

out/$(SITE)/atom-feed.xml: int/merged_index.json \
                src/templates/atom-feed.xml
	mkdir -p $(dir $@)
	chevron \
            src/templates/atom-feed.xml \
	    -d int/merged_index.json \
	    > out/$(SITE)/atom-feed.xml

out/$(SITE)/%: src/static/%
	mkdir -p $(dir $@)
	cp $< $@

.PHONY: clean
clean:
	rm -r int
	rm -r out

.PHONY: FORCE
FORCE:
