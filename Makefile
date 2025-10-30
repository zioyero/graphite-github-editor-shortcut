.PHONY: all icons package clean help

# Extension files to include in the package
EXTENSION_FILES = manifest.json content.js icon16.png icon48.png icon128.png
PACKAGE_NAME = graphite-github-editor-shortcut.zip

# Default target
all: icons package

# Generate icon files
icons:
	@echo "Generating icons..."
	python3 generate_icons.py

# Create a ZIP package for Chrome Web Store
package: $(EXTENSION_FILES)
	@echo "Creating Chrome Web Store package..."
	@rm -f $(PACKAGE_NAME)
	zip -j $(PACKAGE_NAME) $(EXTENSION_FILES)
	@echo "Package created: $(PACKAGE_NAME)"
	@echo "Ready for Chrome Web Store upload!"

# Install Python dependencies
install:
	@echo "Installing Python dependencies..."
	python3 -m pip install --user -r requirements.txt

# Clean generated files
clean:
	@echo "Cleaning up..."
	rm -f icon16.png icon48.png icon128.png
	rm -f $(PACKAGE_NAME)

# Display help
help:
	@echo "Available targets:"
	@echo "  make icons     - Generate icon files"
	@echo "  make package   - Create ZIP file for Chrome Web Store"
	@echo "  make all       - Generate icons and create package (default)"
	@echo "  make install   - Install Python dependencies"
	@echo "  make clean     - Remove generated files"
	@echo "  make help      - Show this help message"
