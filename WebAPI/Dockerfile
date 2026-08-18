FROM mcr.microsoft.com/dotnet/sdk:7.0 AS build-env
WORKDIR /WebAPI
RUN pwd
RUN ls

# Copy everything
COPY . ./
# Restore as distinct layers
RUN dotnet restore
# Build and publish a release
RUN dotnet publish -c Release -o out

# Build runtime image
FROM mcr.microsoft.com/dotnet/aspnet:7.0
WORKDIR /WebAPI

COPY --from=build-env /WebAPI/out .
ENTRYPOINT ["dotnet", "WebAPI.dll"]